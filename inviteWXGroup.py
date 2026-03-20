import time
import pyautogui
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pyperclip import copy

def invite_WX(groupName, inviteName):
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
    copy(groupName)
    send_keys('^v')
    #search_edit.type_keys(groupName, with_spaces=True)

    # 等待搜索结果出现
    time.sleep(1)

    # 定位聊天窗口项
    file_transfer_assist_item = main_win.child_window(title=groupName, control_type="ListItem", found_index=1)
    try:
        #file_transfer_assist_item.wait('visible',timeout=1.5)
        if file_transfer_assist_item.exists("ListItem"):
            file_transfer_assist_item.set_focus()
            file_transfer_assist_item.type_keys('{ENTER}')
    except Exception as e:
        #print("未能在指定时间内找到窗口")
        #search_edit.type_keys('{ESC}')
        search_edit.type_keys('{ESC}')
        errorString = "查不到微信群聊：" + groupName
        return errorString

    #file_transfer_assist_item.set_focus()
    #file_transfer_assist_item.type_keys('{ENTER}')

    # 定位到消息输入框
    message_input = main_win.child_window(title=groupName, control_type="Edit")
    try:
        if message_input.exists("Edit"):
            message_input.set_focus()
    except Exception as e:
        errorString = "定位不到微信群聊：" + groupName
        return errorString



    moreButton = main_win.child_window(title="聊天信息", control_type="Button")
    moreButton.click_input()
    time.sleep(0.5)
    #main_win.print_control_identifiers()
    inviteButton = main_win.child_window(title="添加", control_type="ListItem")
    inviteButton.click_input()


    time.sleep(0.5)
    searchName = main_win.child_window(title="搜索", control_type="Edit",found_index=0)
    searchName.type_keys(inviteName)
    searchName.type_keys('{ENTER}')
    check = main_win.child_window(title="已选择1个联系人", control_type="Text")
    try:
        if check.exists("Text"):
            print("正在添加联系人:"+inviteName)
    except Exception as e:
            searchName.type_keys("{ESC}")
            errorString = "添加失败："+groupName+","+inviteName
            return errorString

    # try:
    #     check.click_input()
    # except Exception as e:
    #     searchName.type_keys("{ESC}")


    inviteButton = main_win.child_window(title="完成", control_type="Button")
    inviteButton.click_input()
    time.sleep(3)

    return "success"
