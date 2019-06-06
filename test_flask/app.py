#Email:dazhuang_python@sina.com

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Dazhuang"

#通过尖角号可以传递参数
@app.route("/home/<name>")
def handle_name(name):
    return name


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
