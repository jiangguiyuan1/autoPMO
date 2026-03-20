from pywinauto.application import Application
from pyperclip import copy
from pywinauto.keyboard import send_keys
from copyFile import *
from pywinauto import Desktop

app = Application(backend="uia").connect(title="微信")
#main_win = app.window(class_name='Qt51514QWindowIcon')

# 尝试查找聊天列表
#main_win.print_control_identifiers()