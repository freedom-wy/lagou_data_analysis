#Email:dazhuag_python@sina.com
from study_flask.app.libs.http_request import HTTP
#引入flask核心app
from flask import current_app


class YuShuBook(object):
    @staticmethod
    def search_by_isbn(isbn):
        isbn_url = "http://t.yushu.im/v2/book/isbn/%s"%isbn
        response = HTTP.get(url=isbn_url)
        #返回一个字典
        return response

    @staticmethod
    def search_by_keyword(keyword,page=1):
        count = current_app.config['PER_PAGE']
        keyword_url = "http://t.yushu.im/v2/book/search?q=%s&count=%s&start=%s"%(keyword,count,YuShuBook.calculage_start(page))
        response = HTTP.get(url=keyword_url)
        return response

    @staticmethod
    def calculage_start(page):
        return (page-1)*current_app.config['PER_PAGE']
