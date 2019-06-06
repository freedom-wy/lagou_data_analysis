#Email:dazhuang_python@sina.com

#render_template用于渲染html模板
from flask import Flask,render_template

app = Flask(__name__)


name = 'dazhuang'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]



@app.route("/")
def index():
    return render_template('index.html',name=name,movies=movies)

#通过尖角号可以传递参数
@app.route("/home/<name>")
def handle_name(name):
    return name


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
