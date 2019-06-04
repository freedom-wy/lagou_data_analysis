#email:dazhuang_python@sina.com

from flask import Flask


#实例化flask
app = Flask(__name__)

#定义路由,当路由中加上了末尾的斜杠，浏览器在请求不加斜杠的路径时会302到加斜杠的路径上
@app.route("/hello/")
#定义视图函数
def hello():
    return "Hello World!"










if __name__ == '__main__':
    #flask启动，并设置debug模式
    app.run(debug=True)