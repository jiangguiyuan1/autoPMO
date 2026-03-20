from pywinauto.application import Application
from pyperclip import copy
from pywinauto.keyboard import send_keys
from copyFile import *
from pywinauto import Desktop

# 连接到正在运行的微信客户端
app = Application(backend="uia").connect(title="微信")

# 定位到微信主窗口
main_win = app.window(class_name='Qt51514QWindowIcon')
main_win.print_control_identifiers()
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
    else:
        print("无效输入，程序中断")
main_win.set_focus()
time.sleep(0.1)
# 定位搜索框
send_keys('^f')
time.sleep(0.2)
#copy("相亲相爱一家人")
copy("打撒咖啡机当升科技")
send_keys('^v')
time.sleep(0.5)
#send_keys('{DOWN 1}')
time.sleep(0.2)
send_keys("{ENTER}")
time.sleep(0.2)
app_window = Desktop(backend="uia").window(
    title="微信",
    class_name="Chrome_WidgetWin_0"
)
if app_window.exists():
    # 窗口存在（搜索不到群聊），执行ALT+F4关闭
    send_keys('%{F4}')
    print("未找到群聊，已关闭提示窗口，程序结束")
    #return  # 或者使用 exit()/sys.exit()

 # 输入消息内容
# message_input.type_keys('1', with_spaces=True)
send_keys('你好，本周补货单，麻烦尽快安排，不足起订量请', with_spaces=True)
send_keys('@' + "planName", with_spaces=True)
send_keys('{ENTER}')
send_keys('沟通', with_spaces=True)
send_keys('@' + "traceName", with_spaces=True)
send_keys('{ENTER}')
send_keys('{ENTER}')

SetClipboardFiles(r"D:\PMO-测试-1\测试_测试1_测试.xlsx")
send_keys('^v')
time.sleep(0.5)
send_keys('{ENTER}')