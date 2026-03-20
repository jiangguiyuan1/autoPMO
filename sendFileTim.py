import time
import re

from openpyxl.styles.builtins import title
from pywinauto.application import Application
from pywinauto.timings import Timings
from pyperclip import copy
from pywinauto.keyboard import send_keys
from copyFile import *


def send_file_TIM(factoryName, filePath,traceName,planName):
    # 连接到正在运行的客户端
    app = Application(backend="uia").connect(title="QQ",class_name="Chrome_WidgetWin_1")

    # 定位到主窗口
    qq = app.window(title="QQ",class_name="Chrome_WidgetWin_1")

    # 确保窗口可见并且设置焦点
    qq.set_focus()
    qq.wait('visible')

    search_edit = qq.child_window(title='搜索', control_type="ComboBox")
    search_edit.click_input()
    copy(factoryName)
    send_keys('^v')
    #qq.type_keys(factoryName, with_spaces=True)
    time.sleep(1)
    qq.type_keys("{ENTER}")

    try:
        time.sleep(0.5)
        errorWin = app.window(title="全网搜索", class_name="Chrome_WidgetWin_1")
        if errorWin.exists("Edit"):
            errorWin.type_keys("{ESC}")
            errorString = "查不到QQ群聊：" + factoryName
            return errorString
    except Exception as e:
        pass

    #title_regex = re.compile(r"{factoryName}.*".format(factoryName=factoryName))
    chat = qq.child_window(title=factoryName,control_type="Edit")

    try:
        if chat.exists("Edit"):
            chat.set_focus()
    except Exception as e:
        errorString = "定位不到QQ群聊：" + factoryName
        return errorString

    # chat.type_keys("1", with_spaces=True)
    chat.type_keys("你好，本周补货单，麻烦尽快安排，不足起订量请", with_spaces=True)
    chat.type_keys('@' + planName, with_spaces=True)
    chat.type_keys('{ENTER}')
    chat.type_keys("沟通", with_spaces=True)
    chat.type_keys('@' + traceName, with_spaces=True)
    chat.type_keys('{ENTER}')
    chat.type_keys('{ENTER}')

    SetClipboardFiles(filePath)
    send_keys('^v')
    time.sleep(0.4)
    chat.type_keys('{ENTER}')
    time.sleep(0.2)
    # fileButton = qq.child_window(title="文件",control_type="Button")
    # fileButton.click_input()
    #
    # # 等待文件选择对话框出现
    # app = Application(backend='win32').connect(title="请选择")
    # win = app["请选择"]
    # win.wait('visible')
    # input = win.child_window(class_name="Edit")
    # input.click_input()  # 点击输入框
    # #print("文件打开"+filePath)
    # copy(filePath)
    # send_keys('^v')
    # #input.type_keys(filePath, pause=0.01, with_spaces=True)  # 输入文件路径
    # win.child_window(title="确认", class_name="Button").click_input()
    # time.sleep(0.15)
    # send_button = qq.child_window(title="发送(1)", control_type="Button")
    # #qq.type_keys("{ENTER}")
    # send_button.click_input()

    return "success"