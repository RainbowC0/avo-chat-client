import requests
from src.globals.constants import TOKEN


def http_get_without_token(url, **kwargs):
    """封装get方法"""
    # 获取请求参数
    params = kwargs.get("params")
    headers = kwargs.get("headers")
    try:
        result = requests.get(url, params=params, headers=headers)
        return result
    except Exception as e:
        print("get请求错误: %s" % e)


def http_post_without_token(url, **kwargs):
    """封装post方法"""
    # 获取请求参数
    params = kwargs.get("params")
    headers = kwargs.get("headers")
    json_dict = kwargs.get("json")
    try:
        result = requests.post(url, params=params, headers=headers, json=json_dict)
        """返回Response对象"""
        return result
    except Exception as e:
        print("post请求错误: %s" % e)


def http_get(url, **kwargs):
    """封装get方法"""
    # 获取请求参数
    params = kwargs.get("params")
    headers = kwargs.get("headers")
    headers["token"] = TOKEN
    try:
        result = requests.get(url, params=params, headers=headers)
        return result
    except Exception as e:
        print("get请求错误: %s" % e)


def http_post(url, **kwargs):
    """封装post方法"""
    # 获取请求参数
    params = kwargs.get("params")
    headers = kwargs.get("headers")
    json_dict = kwargs.get("json")
    headers["token"] = "xxx.xxx.xxx"
    try:
        result = requests.post(url, params=params, headers=headers, json=json_dict)
        """返回Response对象"""
        return result
    except Exception as e:
        print("post请求错误: %s" % e)



