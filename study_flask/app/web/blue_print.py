#Email:dazhuang_python@sina.com



#使用蓝图注册路由
from flask import Blueprint




#实例化蓝图,第一个参数是蓝图的名称，第二个参数是蓝图所在位置，包名
web_blue = Blueprint('web',__name__)