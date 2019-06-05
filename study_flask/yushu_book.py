#Email:dazhuag_python@sina.com

from http_request import HTTP



class YuShuBook(object):
    @staticmethod
    def search_by_isbn(isbn):
        isbn_url = "http://t.yushu.im/v2/book/isbn/%s"%isbn
        response = HTTP.get(url=isbn_url)
        #返回一个字典
        return response

    @staticmethod
    def search_by_keyword(keyword,count=15,start=0):
        keyword_url = "http://t.yushu.im/v2/book/search?q=%s&count=%s&start=%s"%(keyword,count,start)
        response = HTTP.get(url=keyword_url)
        return response
