import time
import pyautogui
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pyperclip import copy

def invite_WX(groupName, inviteName):
    # 连接到正在运行的微信客户端
    app = Application(backend="uia").connect(title="微信")
    # print("ttt")
    # 定位到微信主窗口
    main_win = app.window(class_name='mmui::MainWindow')
    # main_win.print_control_identifiers()
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
    time.sleep(0.1)
    # 定位搜索框
    send_keys('^f')
    time.sleep(0.2)
    send_keys('^a')
    copy(groupName)
    send_keys('^v')
    # .sleep(0.5)
    # send_keys('{DOWN 1}')
    # time.sleep(0.2)
    send_keys("{ENTER}")
    time.sleep(0.2)


    moreButton = main_win.child_window(title="聊天信息", control_type="Button")
    moreButton.click_input()
    time.sleep(0.5)
    main_win.print_control_identifiers()
    inviteButton = main_win.child_window(title="添加")
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
