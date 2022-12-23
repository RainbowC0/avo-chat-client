from src.api.protocol import write_local_token
from src.globals import constants
from src.api.requests_wrapper import http_post, http_post_without_token
from src.exception.business_exception import BusinessException


def user_register(nickname, password):
    """用户注册"""
    payload = {
        "nickname": nickname,
        "password": password
    }
    """result是一个dict类型"""
    result = http_post(constants.USER_REGISTER_URL, json=payload).json()
    if result["code"] == 200:
        print("返回新用户ID为："+result["userID"])
        return result["userID"]
    else:
        raise BusinessException("注册失败："+result["message"])


def user_login(user_id, password):
    """用户登录"""
    payload = {
        "userID": user_id,
        "password": password
    }
    """result是一个dict类型"""
    result = http_post_without_token(constants.USER_LOGIN_URL, json=payload)
    token = result.headers["token"]
    if token:
        print("登录成功，token为："+token)
        constants.TOKEN = token
        write_local_token()
    else:
        raise BusinessException("登录失败："+result["message"])
