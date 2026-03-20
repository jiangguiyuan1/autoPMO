import time

from openpyxl.styles.builtins import title
from pywinauto.application import Application


# QQ 的启动路径
qq_path = r'D:\QQ.exe'  # 请根据实际路径修改
app = Application(backend="uia").start(qq_path)