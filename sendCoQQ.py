import re
import time

import pyautogui
from pywinauto import Application
from pywinauto.keyboard import send_keys
from pyperclip import copy

def send_co_QQ(factoryName, string,traceName,planName):
    # 连接到正在运行的客户端
    app = Application(backend="uia").connect(title="QQ", class_name="Chrome_WidgetWin_1")

    # 定位到主窗口
    qq = app.window(title="QQ", class_name="Chrome_WidgetWin_1")

    # 确保窗口可见并且设置焦点
    qq.set_focus()
    qq.wait('visible')

    #搜索
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

    # title_regex = re.compile(r"{factoryName}.*".format(factoryName=factoryName))
    chat = qq.child_window(title=factoryName, control_type="Edit")

    try:
        if chat.exists("Edit"):
            chat.set_focus()
    except Exception as e:
        errorString = "定位不到QQ群聊：" + factoryName
        return errorString
    chat.type_keys("您好，以下是下单未到货明细，麻烦尽快安排发货", with_spaces=True)
    copy(string)
    send_keys('^v')
    chat.type_keys('{ENTER}')

    # copy("我司中秋、国庆假期仓库作业安排通知：\n9月25日、10月1日-3日共计四天暂停收货、验货、入库。\n烦请贵司提前规划发货，感谢配合！")
    # send_keys('^v')
    # chat.type_keys('{ENTER}')

    return "success"
