import time

from pywinauto.application import Application
from pyperclip import copy
from pywinauto.keyboard import send_keys
from pywinauto import Desktop
from processManger import kill_process_by_name

class QQ:
    def __init__(self):
        self.application = Application(backend="uia").connect(title="QQ",class_name="Chrome_WidgetWin_1")
        self.window = self.application.window(title="QQ",class_name="Chrome_WidgetWin_1")




    def search(self, searchName):
        self.window.set_focus()
        self.window.wait('visible')
        search_edit = self.window.child_window(title='搜索', control_type="ComboBox")
        search_edit.click_input()
        copy(searchName)
        send_keys('^v')
        # qq.type_keys(factoryName, with_spaces=True)
        time.sleep(1)
        self.window.type_keys("{ENTER}")

        try:
            time.sleep(0.5)
            errorWin = self.application.window(title="全网搜索", class_name="Chrome_WidgetWin_1")
            if errorWin.exists("Edit"):
                errorWin.type_keys("{ESC}")
                errorString = "查不到QQ群聊：" + searchName
                return errorString
        except Exception as e:
            pass
        return "success"

    def sendMessage(self, groupName,message):
        result = self.search(groupName)
        if result != "success":
            return result

        chat = self.window.child_window(title=groupName, control_type="Edit")
        try:
            if chat.exists("Edit"):
                chat.set_focus()
        except Exception as e:
            errorString = "定位不到QQ群聊：" + groupName
            return errorString

        chat.type_keys(message, with_spaces=True)
        time.sleep(0.2)
        chat.type_keys('{ENTER}')
        chat.type_keys('{ENTER}')
        return "success"

    def sendFile(self, filePath, groupName,message):
        result = self.sendMessage(groupName, message)
        if result != "success":
            return result

        fileButton = self.window.child_window(title="文件", control_type="Button")
        fileButton.click_input()

        # 等待文件选择对话框出现
        app = Application(backend='win32').connect(title="请选择")
        win = app["请选择"]
        win.wait('visible')
        input = win.child_window(class_name="Edit")
        input.click_input()  # 点击输入框
        copy(filePath)
        send_keys('^v')
        win.child_window(title="确认", class_name="Button").click_input()
        time.sleep(0.1)
        send_button = self.window.child_window(title="发送(1)", control_type="Button")
        send_button.click_input()

        return "success"

    def invite(self, groupName ,inviteName):
        result = self.search(groupName)
        if result != "success":
            return result

        inviteButton = self.window.child_window(title="邀请加群", control_type="Button")
        inviteButton.click_input()
        time.sleep(0.5)
        self.window.type_keys(inviteName)
        time.sleep(0.5)
        self.window.type_keys("{ENTER}")

        checkInvite = self.window.child_window(title="已选 1 个联系人", control_type="Text")
        try:
            if checkInvite.exists("Text"):
                print("正在添加联系人：" + inviteName)
        except Exception as e:
            self.window.type_keys("{ESC}")
            errorString = "添加失败：" + groupName + "," + inviteName
            return errorString

        commitButton = self.window.child_window(title="确定", control_type="Button")
        commitButton.click_input()
        time.sleep(0.5)

        return "success"

    def sendPic(self, filePath, groupName):
        result = self.search(groupName)
        if result != "success":
            return result

        fileButton = self.window.child_window(title="文件", control_type="Button")
        fileButton.click_input()

        # 等待文件选择对话框出现
        app = Application(backend='win32').connect(title="请选择")
        win = app["请选择"]
        win.wait('visible')
        input = win.child_window(class_name="Edit")
        input.click_input()  # 点击输入框
        copy(filePath)
        send_keys('^v')
        win.child_window(title="确认", class_name="Button").click_input()
        time.sleep(0.1)
        send_button = self.window.child_window(title="发送(1)", control_type="Button")
        send_button.click_input()

        return "success"
