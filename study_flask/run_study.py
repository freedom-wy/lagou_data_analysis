#Email:dazhuang_python@sina.com
from study_flask.app import create_app

#引入蓝图
app = create_app()

if __name__ == '__main__':
    #flask启动，并设置debug模式
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=80)