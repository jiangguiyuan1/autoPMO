import time

import pyautogui
from pywinauto import Application

# 连接到正在运行的QQ应用程序
app = Application(backend="uia").connect(title="QQ",class_name="TXGuiFoundation")

# 获取QQ主窗口
qq_main = app.window(title="QQ",class_name="TXGuiFoundation")

# 获取搜索框
search_edit = qq_main.child_window(title_re="搜索", control_type="Edit")
search_edit.click_input()
#搜索联系人
search_edit.type_keys("一坨屎")
# 等待搜索结果出现
time.sleep(0.5)
search_edit.wait('visible')
search_edit.set_focus()
# 进入聊天框
search_edit.type_keys('{ENTER}')
#
search_edit.type_keys("库存系统-新采购单，请查收。")
search_edit.type_keys('{ENTER}')
# 定位聊天窗口项
win=Application(backend="uia").connect(title="一坨屎",class_name="TXGuiFoundation")
chat = win['一坨屎']

location = pyautogui.locateOnScreen("sendImage.png")
x, y =pyautogui.center(location)
pyautogui.click(x, y)
# 等待文件选择对话框出现
app = Application(backend='win32').connect(title_re="打开")
win = app["打开"]
#win.print_control_identifiers()
input = win.child_window(class_name="Edit")
input.click_input()  # 点击输入框
input.type_keys('C:\\Users\\guiyuan.zhang\\Desktop\\PMO\\张桂源PMO2024091500005-9.19-亭亭\\CO2409190962_宁德市沃德汽车配件有限公司_20240919.xls')  # 输入文件路径
win.child_window(title="打开(&O)", class_name="Button").click_input()

search_edit.type_keys("{ESC}")
search_edit.type_keys('{ENTER}')





