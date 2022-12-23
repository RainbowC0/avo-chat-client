from gi.overrides.Gtk import Gtk

from src.exception.business_exception import BusinessException

try:
    import sys
    from concurrent.futures import ThreadPoolExecutor
    from src.globals.constants import MAX_WORKER
    """
        导入自定义模块utils, __init__会自动初始化CACHE_DICT与MESSAGE_STORAGE_DICT
        后续所有对CACHE_DICT与MESSAGE_STORAGE_DICT的操作都是对这两个全局变量的操作
        注册了atexit函数，程序退出时自动调用，会将这两个全局字典变量写入json文件保存
    """
    from src.utils.cache_utils import *
    from src.utils.message_utils import *

    """
       命令行启动参数示例: python3 {path_to_main.py} {python进程的pid} {管道读端文件描述符FD值}
       从命令行参数里提取出当前进程ID和管道读端文件描述符FD值
    """
    argv = sys.argv
    PID = int(argv[1])
    PIPE_FD = int(argv[2])

    """
        通过当前进程ID和管道读端文件描述符FD值拼接出管道读端文件路径，将后续对管道的IO直接转换为文件IO
    """
    PIPE_INPUT_PATH = os.path.join("/proc", str(PID), "fd", str(PIPE_FD))
    print(PIPE_INPUT_PATH)

    """
        加载登录页的UI glade文件
    """
    # log_window = LoginWindow()
    # hd = log_window.get_titlebar()
    # hd.get_style_context().add_provider(log_window.provider, 600)
    # log_window.show()
    # Gtk.main()

except BusinessException as e:
    print(e)
    
except Exception as e:
    print(e)
    exit(-1)
