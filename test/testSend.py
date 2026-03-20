from pywinauto.application import Application


def send_file(factoryName, filePath,traceName):
    # 连接到正在运行的微信客户端
    app = Application(backend="uia").connect(title="微信")

    # 定位到微信主窗口
    main_win = app.window(class_name='WeChatMainWndForPC')

    # 确保微信窗口可见并且设置焦点
    main_win.wait('visible')
    main_win.set_focus()

    # 定位搜索框，这里假设搜索框的标题是 '搜索' 并且控制类型是 "Edit"
    search_edit = main_win.child_window(title='搜索', control_type="Edit")

    # 等待搜索框可用
    search_edit.wait('enabled', timeout=10)

    # 激活搜索框并输入搜索内容
    search_edit.click_input()
    search_edit.type_keys(factoryName, with_spaces=True)

    # 等待搜索结果出现
    # main_win.print_control_identifiers()

    # 定位聊天窗口项
    # 这里的 'title' 需要根据实际的搜索结果进行调整 文件传输助手 广州丰之源-创颖峻采购沟通群
    file_transfer_assist_item = main_win.child_window(title=factoryName, control_type="ListItem", found_index=0)
    file_transfer_assist_item.click_input()

    # 定位到消息输入框，这里假设输入框的标题是 "输入" 并且控制类型是 "Edit"
    message_input = main_win.child_window(title=factoryName, control_type="Edit")
    # 输入消息内容
    message_input.type_keys('库存系统-新采购单，请查收。', with_spaces=True)
    message_input.type_keys('@' + traceName)
    message_input.type_keys('{ENTER}')

    # 定位
    # 这里的 'title' 需要根据实际的搜索结果进行调整
    file_transfer_assist_item = main_win.child_window(title='发送文件', control_type="Button", found_index=0)
    file_transfer_assist_item.click_input()

    # 等待文件选择对话框出现
    app = Application(backend='win32').connect(title_re="打开")
    win = app["打开"]
    #win.print_control_identifiers()
    input = win.child_window(class_name="Edit")
    input.click_input()  # 点击输入框
    input.type_keys(filePath)  # 输入文件路径
    win.child_window(title="打开(&O)", class_name="Button").click_input()
    send_button = main_win.child_window(title="发送（1）", control_type="Button")
    send_button.click_input()



file_dict0 = {'path': 'C:\\Users\\guiyuan.zhang\\Desktop\\PMO\\张桂源PMO2024091500005-9.19-亭亭\\CO2409190962_宁德市沃德汽车配件有限公司_20240919.xls', 'name': '文件传输助手','searchName':'文件传输助手','traceName':'江桂圆'}
file_dict1 = {'path': 'C:\\Users\\guiyuan.zhang\\Desktop\\PMO\\张桂源PMO2024091500005-慧珍\\CO2409191032_深圳市征途汽车用品有限公司_20240919.xls', 'name': '文件传输助手','searchName':'文件传输助手','traceName':'江桂圆'}
file_dict2 = {'path': 'C:\\Users\\guiyuan.zhang\\Desktop\\PMO\\张桂源PMO2024091500005楚汶\\CO2409191464_深圳概动电子科技有限公司_20240919.xls', 'name': '文件传输助手','searchName':'文件传输助手','traceName':'江桂圆'}

files_array = []
files_array.append(file_dict0)
files_array.append(file_dict1)
files_array.append(file_dict2)


for file_dict in files_array:
    #print(file_dict.get('searchName'),file_dict['path'],file_dict['traceName'])
    send_file(file_dict['searchName'],file_dict['path'],file_dict['traceName'])

