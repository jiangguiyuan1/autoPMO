import psutil
import time

from pywinauto import Desktop
from pywinauto.application import Application

# for proc in psutil.process_iter(['pid', 'name']):
#     print(proc.info['name'])

def kill_process_by_name(process_name):
    """
    杀掉指定名称的进程
    :param process_name: 进程名称
    """
    # 遍历所有进程
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # 获取进程名称
            if proc.info['name'] == process_name:
                print(f"找到进程 {process_name}，PID: {proc.info['pid']}")
                # 杀掉进程
                proc.terminate()
                print(f"已杀掉进程 {process_name}，PID: {proc.info['pid']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def check_QQ():
    # 获取桌面上的所有窗口
    dlgs = Desktop(backend="uia").windows()
    # 检查是否有两个或更多的窗口标题包含 "QQ"
    qq_windows = [dlg for dlg in dlgs if "QQ" in dlg.window_text()]

    # 判断是否存在两个或更多的 "QQ" 窗口
    if len(qq_windows) >= 2 or len(qq_windows) == 0 :
        kill_process_by_name('QQ.exe')

        # 等待 QQ 窗口打开
        time.sleep(1)

        # QQ 的启动路径
        qq_path = r'D:\QQ.exe'  # 请根据实际路径修改
        app = Application(backend="uia").start(qq_path)

        # 等待 QQ 窗口打开
        time.sleep(3)

        print("请确认QQ登录状态，输入 Y/N 继续运行：", end='')
        user_input = input().strip().upper()
        if user_input == 'Y':
            return 'success'
        elif user_input == 'N':
            print("程序中断")
            return "QQ未登录"
        else:
            print("无效输入，程序中断")
            return "QQ未登录"

    return 'success'
