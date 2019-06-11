#Email:dazhuag_python@sina.com
from app.libs.http_request import HTTP
#引入flask核心app
from flask import current_app


class YuShuBook(object):
    def __init__(self):
        self.total = 0
        self.books = []

    #通过isbn号搜索
    def search_by_isbn(self,isbn):
        isbn_url = "http://t.yushu.im/v2/book/isbn/%s"%isbn
        response = HTTP.get(url=isbn_url)
        self.__fill_single(data=response)

    #通过关键字搜索
    def search_by_keyword(self,keyword,page=1):
        count = current_app.config['PER_PAGE']
        keyword_url = "http://t.yushu.im/v2/book/search?q=%s&count=%s&start=%s"%(keyword,count,self.calculage_start(page))
        response = HTTP.get(url=keyword_url)
        self.__file_collection(data=response)

    def calculage_start(self,page):
        return (page-1)*current_app.config['PER_PAGE']

    def __fill_single(self,data):
        """
        处理ISBN搜索的返回数据
        :param data: 原始数据
        :return:
        """
        if data:
            self.total = 1
            self.books.append(data)

    def __file_collection(self,data):
        """
        处理关键字搜索的返回数据
        :param data: 原始数据
        :return:
        """
        self.total = data['total']
        self.books = data['books']





class __YuShuBook(object):
    @staticmethod
    #通过isbn号搜索
    def search_by_isbn(isbn):
        isbn_url = "http://t.yushu.im/v2/book/isbn/%s"%isbn
        response = HTTP.get(url=isbn_url)
        #返回一个字典
        return response

    @staticmethod
    #通过关键字搜索
    def search_by_keyword(keyword,page=1):
        count = current_app.config['PER_PAGE']
        keyword_url = "http://t.yushu.im/v2/book/search?q=%s&count=%s&start=%s"%(keyword,count,YuShuBook.calculage_start(page))
        response = HTTP.get(url=keyword_url)
        return response

    @staticmethod
    def calculage_start(page):
        return (page-1)*current_app.config['PER_PAGE']
