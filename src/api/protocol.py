import json

from src.globals.constants import T_P2P, T_P2G, TOKEN


def __read_a_json_from_pipe(pipe):
    """从管道中读取一个json，供pipe_listener函数调用"""
    json_size = int(pipe.read(4))
    if json_size == 0:
        return None
    json_str = pipe.read(json_size)
    return json.loads(json_str)


def pipe_listener(pipe_output_path):
    with open(pipe_output_path, "r") as pipe:
        while True:
            notify = __read_a_json_from_pipe(pipe)
            print(notify)
            if notify is None:
                print("pipe closed")
                break
            if notify["type"] == T_P2P:
                # TODO：根据notify里的puller和pull_target字段,以及本地“最新”消息时间向服务器请求消息
                pass
            elif notify["type"] == T_P2G:
                pass


def read_local_token():
    """读本地保存的TOKEN文件"""
    with open("storage/token.txt", "r") as f:
        return f.read()


def write_local_token():
    """将全局变量TOKEN写入本地文件"""
    with open("storage/token.txt", "w") as f:
        f.write(TOKEN)
