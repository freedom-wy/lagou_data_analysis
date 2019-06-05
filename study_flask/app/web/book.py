#Email:dazhuang_python@sina.com


from flask.json import jsonify
from study_flask.app.web.blue_print import web_blue
from study_flask.helper import isbn_or_key
from study_flask.yushu_book import YuShuBook


#定义路由,当路由中加上了末尾的斜杠，浏览器在请求不加斜杠的路径时会302到加斜杠的路径上
#通过q和page传递参数
#更改为通过蓝图注册,蓝图最终还需要注册到app上
@web_blue.route("/book/search/<q>/<page>")
#定义视图函数
def search(q,page):
    #判断传入的q是ISBN还是普通关键字
    isbn_or_key_value = isbn_or_key(q)
    if isbn_or_key_value == 'isbn':
        result = YuShuBook.search_by_isbn(isbn=q)
    else:
        result = YuShuBook.search_by_keyword(keyword=q)
    return jsonify(result)