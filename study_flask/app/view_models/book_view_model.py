#Email:dazhuang_python@sina.com
#引入view-models

class BookViewModel:
    #用于解决数据规范性
    #单本书
    @classmethod
    def package_single(cls,data,keyword):
        '''
        :param data: 原始数据
        :param keyword: 关键字
        :return: info
        '''
        info = {
            "books":[],
            #总条数
            "total":0,
            "keyword":keyword
        }
        if data:
            info['total'] = 1
            info['books'] = [cls.__cut_book_data(data)]
        return info

    #多本书
    @classmethod
    def package_collection(cls,data,keyword):
        info = {
            "books":[],
            #总条数
            "total":0,
            "keyword":keyword
        }
        if data:
            info['total'] = data['total']
            info['books'] = [cls.__cut_book_data(data=book) for book in data['books']]
        return info

    @classmethod
    def __cut_book_data(cls,data):
        """
        用于修饰数据，完善，裁剪等
        :return: 返回修剪后的数据book
        """
        book = {
            "title":data['title'],
            "publisher":data['publisher'] or "",
            "pages":data['pages'] or "",
            "price":data['price'] or "",
            "summary":data['summary'] or "",
            "image":data['image'] or "",
            #由于鱼书api返回的作者是列表，因此使用join方法处理
            "author":",".join(data['author'])
        }
        return book
