#Email:dazhuang_python@sina.com

from flask import Flask, make_response

#实例化flask
app = Flask(__name__)
#读取配置文件
app.config.from_object('config')

#定义路由,当路由中加上了末尾的斜杠，浏览器在请求不加斜杠的路径时会302到加斜杠的路径上
@app.route("/hello/")
#定义视图函数
def hello():
    #定义返回头部
    headers = {
        "content-type":"html/text",
        "location":"https://www.baidu.com"
    }
    #定义返回内容
    response = make_response("",301)
    response.headers = headers
    #向浏览器返回内容
    return response










if __name__ == '__main__':
    #flask启动，并设置debug模式
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=80)