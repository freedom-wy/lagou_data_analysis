#Email:dazhuang_python@sina.com


from flask import Flask
from study_flask.app.web.blue_print import web_blue


#将初始化代码放入__init__文件中
def create_app():
    #实例化flask
    app = Flask(__name__)
    #读取配置文件
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    #调用注册函数
    register_blueprint_func(app)
    return app

#注册蓝图到app上
def register_blueprint_func(app):
    app.register_blueprint(web_blue)