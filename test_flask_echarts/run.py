from flask import Flask, render_template, jsonify

# 实例化flask
app = Flask(__name__)

# 注册路由
@app.route("/")
def index():
    return "Hello World"

@app.route("/get_data")
def get_data():
    data = {"name":['商超门店', '教育培训', '房地产', '生活服务', '汽车销售', '旅游酒店', '五金建材']}
    return jsonify(data)


@app.route("/lagou/",methods=['GET','POST'])
def lagou():
    return render_template('index.html')
    # return render_template('hello.html')

@app.route("/user/<username>")
def show_user_profile(username):
    return "User %s"%username

if __name__ == '__main__':
    # 启动flask
    app.run(debug = True,host="0.0.0.0",port=80)