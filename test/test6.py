import time

from pywinauto.application import Application
from pyperclip import copy
from pywinauto.keyboard import send_keys
from copyFile import *


# 连接到正在运行的微信客户端
app = Application(backend="uia").connect(title="微信")

# 定位到微信主窗口
main_win = app.window(class_name='WeChatMainWndForPC')

# 确保微信窗口可见并且设置焦点
main_win.wait('visible')
main_win.set_focus()
#main_win.print_control_identifiers()

# 定位搜索框，这里假设搜索框的标题是 '搜索' 并且控制类型是 "Edit"
search_edit = main_win.child_window(title='搜索', control_type="Edit")

# 等待搜索框可用
search_edit.wait('enabled', timeout=10)

# 激活搜索框并输入搜索内容
search_edit.click_input()

search_edit.type_keys("广州瑞达abs传感器&创颖峻", with_spaces=True)

# 等待搜索结果出现
time.sleep(1)
main_win.print_control_identifiers()
# search_edit.wait('visible')
# search_edit.set_focus()
# 定位聊天窗口项
file_transfer_assist_item = main_win.child_window(title="广州瑞达abs传感器&创颖峻", control_type="ListItem", found_index=1)
#file_transfer_assist_item.print_control_identifiers()
try:
    # file_transfer_assist_item.wait('visible',timeout=1.5)
    if file_transfer_assist_item.exists("ListItem"):
        file_transfer_assist_item.set_focus()
        file_transfer_assist_item.type_keys('{ENTER}')
except Exception as e:
    print("未能在指定时间内找到窗口")
    # search_edit.type_keys('{ESC}')
    search_edit.type_keys('{ESC}')


# file_transfer_assist_item.set_focus()
# file_transfer_assist_item.type_keys('{ENTER}')

# 定位到消息输入框
message_input = main_win.child_window(title="广州瑞达abs传感器&创颖峻", control_type="Edit")
try:
    if message_input.exists("Edit"):
        message_input.set_focus()
except Exception as e:
    errorString = "定位不到微信群聊：" + "广州瑞达abs传感器&创颖峻"

# 输入消息内容
# message_input.type_keys('1', with_spaces=True)
message_input.type_keys('你好，本周补货单，麻烦尽快安排，不足起订量请', with_spaces=True)