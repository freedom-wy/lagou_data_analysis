#Email:dazhuang_python@sina.com

def isbn_or_key(word):
    """
    判断传入的word是ISBN编号还是关键字
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    # 判断ISBN号是否为13位和是否全为数字
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    # 对10位isbn号进行替换
    short_word = word.replace("-", "")
    # 判断是否为10为ISBN和是否全为数字
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key