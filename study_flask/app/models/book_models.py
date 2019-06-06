#Email:dazhuang_python@sina.com
from sqlalchemy import Column, Integer, String
#导入flask_sqlchemy
from flask_sqlalchemy import SQLAlchemy


#实例化
db = SQLAlchemy()


#需要继承db.model
#需要在核心对象中注册,关联
class Book(db.Model):
    #设置为主键自增长
    id = Column(Integer,primary_key=True,autoincrement=True)
    #设置书名不能为空
    title = Column(String(50),nullable=False)
    author = Column(String(30),default="佚名")
    #平装还是精装
    binding = Column(String(20))
    #出版社
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    #设置ISBN编号不能为空，并且不重复
    isbn = Column(String(15),nullable=False,unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
