from pywinauto.application import Application
from pyperclip import copy
from pywinauto.keyboard import send_keys
from copyFile import *
from pywinauto import Desktop

def send_co_WX_V2(factoryName, string,traceName,planName):
    # 连接到正在运行的微信客户端
    app = Application(backend="uia").connect(title="微信")

    # 定位到微信主窗口
    main_win = app.window(class_name='mmui::MainWindow')
    #main_win.print_control_identifiers()
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
    copy(factoryName)
    send_keys('^v')
    # .sleep(0.5)
    # send_keys('{DOWN 1}')
    # time.sleep(0.2)
    send_keys("{ENTER}")
    time.sleep(0.2)


     # 输入消息内容
    # message_input.type_keys('1', with_spaces=True)
    # 输入消息内容
    send_keys("您好,以下是下单未到货明细,麻烦尽快安排发货", with_spaces=True)
    time.sleep(0.2)
    send_keys('{DOWN 1}')
    send_keys('{ENTER}')

    app_window = Desktop(backend="uia").window(
        title="微信",
        class_name="Chrome_WidgetWin_0"
    )
    if app_window.exists():
        # 窗口存在（搜索不到群聊），执行ALT+F4关闭
        send_keys('%{F4}')
        # print("未找到群聊，已关闭提示窗口，程序结束")
        errorString = "查不到微信群聊：" + factoryName
        return errorString

    copy(string)
    send_keys('^v')
    send_keys('{ENTER}')

    # copy("我司中秋、国庆假期仓库作业安排通知：\n9月25日、10月1日-3日共计四天暂停收货、验货、入库。\n烦请贵司提前规划发货，感谢配合！")
    # send_keys('^v')
    # send_keys('{ENTER}')


    return "success"