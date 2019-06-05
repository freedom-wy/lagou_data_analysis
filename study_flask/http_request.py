#Email:dazhuang_python@sina.com
import requests

#名字不要起为http.py会与当前Python中http包冲突
class HTTP(object):
    #发送http的get请求
    @staticmethod
    def get(url,return_json=True):
        response = requests.get(url=url)
        #如果请求失败则返回空字段或''
        if response.status_code != 200:
            return {} if return_json else ''
        #如果请求成功则正常返回
        return response.json() if return_json else response.text