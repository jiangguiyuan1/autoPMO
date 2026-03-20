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
    send_keys("您好，以下是下单未到货明细，麻烦尽快安排发货", with_spaces=True)
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

    # copy("尊敬的各位供应商伙伴：\n新春佳节将至，结合我司仓库工作安排，现将春节前后收货时间通知如下：\n1、 节前最后收货时间：2月10日。\n2、 春节后恢复收货时间：2月24日起正常收货。\n请各位合作伙伴协调好发货计划，确保需在节前送达的货物于 2月10日前送达我司仓库。若货物无法在2月10日前送达，请安排春节后（2月24日起）再行发货。\n感谢您的支持与配合！预祝各位新春快乐，阖家安康！")
    # send_keys('^v')
    # send_keys('{ENTER}')

    return "success"