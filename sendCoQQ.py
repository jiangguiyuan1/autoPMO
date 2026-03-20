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

    # copy("尊敬的各位供应商伙伴：\n新春佳节将至，结合我司仓库工作安排，现将春节前后收货时间通知如下：\n1、 节前最后收货时间：2月10日。\n2、 春节后恢复收货时间：2月24日起正常收货。\n请各位合作伙伴协调好发货计划，确保需在节前送达的货物于 2月10日前送达我司仓库。若货物无法在2月10日前送达，请安排春节后（2月24日起）再行发货。\n感谢您的支持与配合！预祝各位新春快乐，阖家安康！")
    # send_keys('^v')
    # chat.type_keys('{ENTER}')

    return "success"
