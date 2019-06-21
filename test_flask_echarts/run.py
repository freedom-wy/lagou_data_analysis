from flask import Flask,render_template

# 实例化flask
app = Flask(__name__)

# 注册路由
@app.route("/")
def index():
    return "Hello World"

@app.route("/lagou/",methods=['GET','POST'])
def lagou():
    return render_template('index.html')

@app.route("/user/<username>")
def show_user_profile(username):
    return "User %s"%username

if __name__ == '__main__':
    # 启动flask
    app.run(debug = True,host="0.0.0.0",port=80)