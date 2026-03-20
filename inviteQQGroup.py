import time
import re

from openpyxl.styles.builtins import title
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pyperclip import copy

def invite_QQ(groupName, inviteName):
    # 连接到正在运行的客户端
    app = Application(backend="uia").connect(title="QQ",class_name="Chrome_WidgetWin_1")

    # 定位到主窗口
    qq = app.window(title="QQ",class_name="Chrome_WidgetWin_1")

    # 确保窗口可见并且设置焦点
    qq.set_focus()
    qq.wait('visible')

    search_edit = qq.child_window(title='搜索', control_type="ComboBox")
    search_edit.click_input()
    copy(groupName)
    send_keys('^v')
    #qq.type_keys(groupName, with_spaces=True)
    time.sleep(1)
    qq.type_keys("{ENTER}")

    # #title_regex = re.compile(r"{factoryName}.*".format(factoryName=factoryName))
    # chat = qq.child_window(title=groupName,control_type="Edit")
    # try:
    #     if chat.exists("Edit"):
    #         chat.click_input()
    # except Exception as e:
    #     time.sleep(1)
    #     app.window(title="全网搜索", class_name="Chrome_WidgetWin_1").type_keys("{ESC}")
    #     errorString = "查不到QQ群聊：" +groupName
    #     return errorString
    try:
        time.sleep(0.5)
        errorWin = app.window(title="全网搜索", class_name="Chrome_WidgetWin_1")
        if errorWin.exists("Edit"):
            errorWin.type_keys("{ESC}")
            errorString = "查不到QQ群聊：" + groupName
            return errorString
    except Exception as e:
        pass

    #title_regex = re.compile(r"{factoryName}.*".format(factoryName=factoryName))
    chat = qq.child_window(title=groupName,control_type="Edit")

    try:
        if chat.exists("Edit"):
            chat.set_focus()
    except Exception as e:
        errorString = "定位不到QQ群聊：" + groupName
        return errorString

    inviteButton = qq.child_window(title="邀请加群",control_type="Button")
    inviteButton.click_input()
    time.sleep(0.5)
    qq.type_keys(inviteName)
    time.sleep(0.5)
    qq.type_keys("{ENTER}")

    checkInvite = qq.child_window(title="已选 1 个联系人", control_type="Text")
    try:
        if checkInvite.exists("Text"):
            print("正在添加联系人："+inviteName)
    except Exception as e:
            qq.type_keys("{ESC}")
            errorString = "添加失败："+groupName+","+inviteName
            return errorString
    # try:
    #     checkInvite.click_input()
    # except Exception as e:
    #     qq.type_keys("{ESC}")
    # checkInvite.click_input()


    commitButton = qq.child_window(title="确定", control_type="Button")
    commitButton.click_input()

    time.sleep(0.5)

    return "success"