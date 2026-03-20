import re
import time

import pyautogui
from pywinauto import Application
from pywinauto.keyboard import send_keys


def send_file_QQ(factoryName, filePath,traceName):
    # 连接到正在运行的QQ应用程序
    app = Application(backend="uia").connect(title="QQ",class_name="TXGuiFoundation")

    # 获取QQ主窗口
    qq_main = app.window(title="QQ",class_name="TXGuiFoundation")

    # 获取搜索框
    search_edit = qq_main.child_window(title_re="搜索", control_type="Edit")
    search_edit.click_input()
    #搜索联系人
    search_edit.type_keys(factoryName, with_spaces=True)
    # 等待搜索结果出现
    time.sleep(0.5)
    search_edit.wait('visible')
    search_edit.set_focus()
    # 进入聊天框
    search_edit.type_keys('{ENTER}')
    #发送消息
    search_edit.type_keys("库存系统-新补货单，请查收。")
    search_edit.type_keys("下单相关问题请联系@"+traceName)
    search_edit.type_keys("{ENTER}")
    search_edit.type_keys("{ENTER}")

    title_regex= re.compile(r"{factoryName}.*".format(factoryName=factoryName[:3]))
    # 定位聊天窗口项
    win=Application(backend="uia").connect(title_re=title_regex,class_name="TXGuiFoundation")
    chat = win[factoryName]
    # 定位到发送文件
    location = pyautogui.locateOnScreen("sendImage.png")
    x, y =pyautogui.center(location)
    pyautogui.click(x, y)
    # 等待文件选择对话框出现
    app = Application(backend='win32').connect(title_re="打开")
    win = app["打开"]
    win.wait('visible')
    #win.print_control_identifiers()
    input = win.child_window(class_name="Edit")
    input.click_input()  # 点击输入框
    input.type_keys(filePath, pause=0.01, with_spaces=True)  # 输入文件路径
    win.child_window(title="打开(&O)", class_name="Button").click_input()
    time.sleep(1.5)
    #退出
    search_edit.type_keys('{ESC}')
    search_edit.type_keys('{ENTER}')





