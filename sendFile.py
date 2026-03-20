import time

from pywinauto.application import Application
from pyperclip import copy
from pywinauto.keyboard import send_keys
from copyFile import *

def send_file(factoryName, filePath,traceName,planName):
    # 连接到正在运行的微信客户端
    app = Application(backend="uia").connect(title="微信")

    # 定位到微信主窗口
    main_win = app.window(class_name='WeChatMainWndForPC')

    # 确保微信窗口可见并且设置焦点
    try:
        main_win.wait('visible')
    except Exception as e:
        print("\n发生错误：", e)
        print("请确认微信登录状态，输入 Y/N 继续运行：", end='')
        user_input = input().strip().upper()
        if user_input == 'Y':
            main_win.wait('visible')
        elif user_input == 'N':
            print("程序中断")
            return "微信未登录"
        else:
            print("无效输入，程序中断")
            return "微信未登录"
    main_win.set_focus()

    # 定位搜索框，这里假设搜索框的标题是 '搜索' 并且控制类型是 "Edit"
    search_edit = main_win.child_window(title='搜索', control_type="Edit")

    # 等待搜索框可用
    search_edit.wait('enabled', timeout=10)

    # 激活搜索框并输入搜索内容
    search_edit.click_input()
    copy(factoryName)
    send_keys('^v')
    #search_edit.type_keys(factoryName, with_spaces=True)

    # 等待搜索结果出现
    time.sleep(1)
    # search_edit.wait('visible')
    # search_edit.set_focus()

    # 定位聊天窗口项
    file_transfer_assist_item = main_win.child_window(title=factoryName, control_type="ListItem", found_index=1)
    try:
        #file_transfer_assist_item.wait('visible',timeout=1.5)
        if file_transfer_assist_item.exists("ListItem"):
            file_transfer_assist_item.set_focus()
            file_transfer_assist_item.type_keys('{ENTER}')
    except Exception as e:
        #print("未能在指定时间内找到窗口")
        #search_edit.type_keys('{ESC}')
        search_edit.type_keys('{ESC}')
        errorString = "查不到微信群聊：" + factoryName
        return errorString

    #file_transfer_assist_item.set_focus()
    #file_transfer_assist_item.type_keys('{ENTER}')

    # 定位到消息输入框
    message_input = main_win.child_window(title=factoryName, control_type="Edit")
    try:
        if message_input.exists("Edit"):
            message_input.set_focus()
    except Exception as e:
        errorString = "定位不到微信群聊：" + factoryName
        return errorString

    # 输入消息内容
    # message_input.type_keys('1', with_spaces=True)
    message_input.type_keys('你好，本周补货单，麻烦尽快安排，不足起订量请', with_spaces=True)
    message_input.type_keys('@' + planName, with_spaces=True)
    message_input.type_keys('{ENTER}')
    message_input.type_keys('沟通', with_spaces=True)
    message_input.type_keys('@' + traceName, with_spaces=True)
    message_input.type_keys('{ENTER}')
    message_input.type_keys('{ENTER}')

    message_input.click_input()
    SetClipboardFiles(filePath)
    send_keys('^v')
    time.sleep(0.5)
    message_input.type_keys('{ENTER}')

    # # 定位
    # file_transfer_assist_item = main_win.child_window(title='发送文件', control_type="Button", found_index=0)
    # file_transfer_assist_item.click_input()
    #
    # # 等待文件选择对话框出现
    # app = Application(backend='win32').connect(title_re="打开")
    # win = app["打开"]
    # win.wait('visible')
    # #win.print_control_identifiers()
    # input = win.child_window(class_name="Edit")
    # input.click_input()  # 点击输入框
    # copy(filePath)
    # send_keys('^v')
    # #input.type_keys(filePath, pause=0.01, with_spaces=True)  # 输入文件路径
    # win.child_window(title="打开(&O)", class_name="Button").click_input()
    # #main_win.type_keys('{ENTER}')
    # send_button = main_win.child_window(title="发送（1）", control_type="Button")
    # send_button.click_input()

    return "success"