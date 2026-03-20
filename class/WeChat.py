import time

from pywinauto.application import Application
from pyperclip import copy
from pywinauto.keyboard import send_keys

class WeChat:
    def __init__(self):
        self.application = Application(backend="uia").connect(title="微信")
        self.window = self.application.window(class_name='WeChatMainWndForPC')


    def load(self):
        print(1)

    def search(self, searchName):
        self.window.set_focus()
        self.window.wait('visible')
        search_edit = (self.window.child_window(title='搜索', control_type="Edit"))
        search_edit.click_input()
        copy(searchName)
        send_keys('^v')
        time.sleep(1)
        # 定位聊天窗口项
        file_transfer_assist_item = self.window.child_window(title=searchName, control_type="ListItem", found_index=1)
        try:
            # file_transfer_assist_item.wait('visible',timeout=1.5)
            if file_transfer_assist_item.exists("ListItem"):
                file_transfer_assist_item.set_focus()
                file_transfer_assist_item.type_keys('{ENTER}')
        except Exception as e:
            # print("未能在指定时间内找到窗口")
            # search_edit.type_keys('{ESC}')
            search_edit.type_keys('{ESC}')
            errorString = "查不到微信群聊：" + searchName
            return errorString
        return "success"

    def sendMessage(self, groupName,message):
        result = self.search(groupName)
        if result!="success":
            return result
        # 定位到消息输入框
        message_input = self.window.child_window(title=groupName, control_type="Edit")
        try:
            if message_input.exists("Edit"):
                message_input.set_focus()
        except Exception as e:
            errorString = "定位不到微信群聊：" + groupName
            return errorString

        # 输入消息内容
        message_input.type_keys(message, with_spaces=True)
        time.sleep(0.2)
        message_input.type_keys('{ENTER}')
        message_input.type_keys('{ENTER}')
        return "success"

    def sendFile(self, filePath, groupName,message):
        result = self.sendMessage( groupName,message)
        if result != "success":
            return result
        # 定位
        file_transfer_assist_item = self.window.child_window(title='发送文件', control_type="Button", found_index=0)
        file_transfer_assist_item.click_input()

        # 等待文件选择对话框出现
        app = Application(backend='win32').connect(title_re="打开")
        win = app["打开"]
        win.wait('visible')
        input = win.child_window(class_name="Edit")
        input.click_input()  # 点击输入框
        copy(filePath)
        send_keys('^v')
        win.child_window(title="打开(&O)", class_name="Button").click_input()
        send_button = self.window.child_window(title="发送（1）", control_type="Button")
        send_button.click_input()

        return "success"

    def invite(self,groupName, inviteName):
        result = self.search(groupName)
        if result != "success":
            return result

        moreButton = self.window.child_window(title="聊天信息", control_type="Button")
        moreButton.click_input()
        time.sleep(0.5)
        # main_win.print_control_identifiers()
        inviteButton = self.window.child_window(title="添加", control_type="ListItem")
        inviteButton.click_input()

        time.sleep(0.5)
        searchName = self.window.child_window(title="搜索", control_type="Edit", found_index=0)
        searchName.type_keys(inviteName)
        searchName.type_keys('{ENTER}')
        check = self.window.child_window(title="已选择1个联系人", control_type="Text")
        try:
            if check.exists("Text"):
                print("正在添加联系人:" + inviteName)
        except Exception as e:
            searchName.type_keys("{ESC}")
            errorString = "添加失败：" + groupName + "," + inviteName
            return errorString

        inviteButton = self.window.child_window(title="完成", control_type="Button")
        inviteButton.click_input()
        time.sleep(1)

        return "success"

    def sendPic(self, filePath, groupName):
        result = self.search(groupName)
        if result != "success":
            return result
        # 定位
        file_transfer_assist_item = self.window.child_window(title='发送文件', control_type="Button", found_index=0)
        file_transfer_assist_item.click_input()

        # 等待文件选择对话框出现
        app = Application(backend='win32').connect(title_re="打开")
        win = app["打开"]
        win.wait('visible')
        input = win.child_window(class_name="Edit")
        input.click_input()  # 点击输入框
        copy(filePath)
        send_keys('^v')
        win.child_window(title="打开(&O)", class_name="Button").click_input()
        send_button = self.window.child_window(title="发送（1）", control_type="Button")
        send_button.click_input()

        return "success"
