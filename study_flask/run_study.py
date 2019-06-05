#Email:dazhuang_python@sina.com

from flask import Flask
from study_flask.helper import isbn_or_key

#实例化flask
app = Flask(__name__)
#读取配置文件
app.config.from_object('config')

#定义路由,当路由中加上了末尾的斜杠，浏览器在请求不加斜杠的路径时会302到加斜杠的路径上
#通过q和page传递参数
@app.route("/book/search/<q>/<page>")
#定义视图函数
def search(q,page):
    #判断传入的q是ISBN还是普通关键字
    isbn_or_key_value = isbn_or_key(q)
    pass










if __name__ == '__main__':
    #flask启动，并设置debug模式
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=80)