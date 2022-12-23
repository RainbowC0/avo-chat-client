import atexit
import json
import os

"""
    缓存信息
    cache_dict为全局变量，字典类型
    可保存userID和password等等
"""
CACHE_DICT = {}


def load_cache_from_file():
    global CACHE_DICT
    if os.path.exists("storage/cache.json"):
        with open("storage/cache.json", "r", encoding="utf-8") as f:
            CACHE_DICT = json.load(f)


def get_cached_user_id():
    return CACHE_DICT.get("userID")


def get_cached_user_password():
    return CACHE_DICT.get("password")


@atexit.register
def write_cache_to_file():
    """注册为atexit函数，程序退出时自动调用"""
    print("write_cache_to_file")
    with open("storage/cache.json", "w", encoding="utf-8") as f:
        json.dump(CACHE_DICT, f, ensure_ascii=False, indent=4)
