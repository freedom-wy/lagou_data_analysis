#Email:dazhuang_python@sina.com
from flask import request, render_template
from flask.json import jsonify
from app.forms.book_forms import SearchForm
from app.view_models.book_view_model import BookCollection
from app.web.blue_print import web_blue
from app.libs.helper import isbn_or_key
from app.spider.yushu_book import YuShuBook
import json


@web_blue.route("/")
def index():
    r = {
        "name":"dazhuang",
        "age":20
    }
    #使用render_template渲染html
    return render_template('test1.html',data=r)

#定义路由,当路由中加上了末尾的斜杠，浏览器在请求不加斜杠的路径时会302到加斜杠的路径上
#通过q和page传递参数
#更改为通过蓝图注册,蓝图最终还需要注册到app上
@web_blue.route("/book/search/")
#定义视图函数
def search():
    form = SearchForm(request.args)
    books = BookCollection()
    #使用validate启用验证
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        #判断传入的q是ISBN还是普通关键字
        isbn_or_key_value = isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key_value == 'isbn':
            yushu_book.search_by_isbn(isbn=q)
        else:
            yushu_book.search_by_keyword(keyword=q,page=page)
        books.fill(yushu_book=yushu_book,keyword=q)
        # return jsonify(books)
        return json.dumps(books,default = lambda o:o.__dict__)
    else:
        return jsonify({"msg":"传入参数有误"})