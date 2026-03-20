import time

from pywinauto.application import Application
from pyperclip import copy
from pywinauto.keyboard import send_keys
from copyFile import *

class DD:
    def __init__(self):
        self.application = Application(backend="uia").connect(title="钉钉",class_name="DtMainFrameView")
        self.window = self.application.window(title="DingTalk",class_name="DtMainFrameView")


    def load(self):
        self.window.set_focus()
        #self.window.wait('visible')
        self.window.print_control_identifiers()

    def search(self, searchName):
        self.window.set_focus()
        self.window.wait('visible')
        #self.window.print_control_identifiers()
        #search_edit = self.window.child_window(title='搜索', control_type="Edit")
        #search_edit.click_input()
        send_keys('^f')
        time.sleep(0.5)
        send_keys('^a')
        time.sleep(0.5)
        copy(searchName)
        send_keys('^v')
        time.sleep(1)
        send_keys("{ENTER}")

    def sendFile(self, filePath):
        #self.window.print_control_identifiers()
        try:
            chat = self.window.child_window(
                auto_id="qt_chat_navigable_content_widget.stackedWidget.mesasgePage.widget.splitter.widgetRichEditWnd.drich_edit.verticalContentWidget.widget_input_wnd",
                control_type="Group")
        except Exception as e:
            print("定位不到钉钉聊天窗口")
            return
        chat.click_input()
        time.sleep(0.4)
        send_keys('^a')
        SetClipboardFiles(filePath)
        send_keys('^v')
        time.sleep(0.2)
        ensure = self.window.child_window(title="确定", control_type="Button")
        ensure.click_input()



