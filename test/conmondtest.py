import os
import re
import pandas as pd
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
    search_edit.wait('visible')
    search_edit.set_focus()

    # 定位聊天窗口项
    file_transfer_assist_item = main_win.child_window(title=factoryName, control_type="ListItem", found_index=1)
    file_transfer_assist_item.wait('visible')
    file_transfer_assist_item.set_focus()
    file_transfer_assist_item.type_keys('{ENTER}')

    # 定位到消息输入框
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
    win.print_control_identifiers()
    input = win.child_window(class_name="Edit")
    input.click_input()  # 点击输入框
    input.type_keys(filePath)  # 输入文件路径
    win.child_window(title="打开(&O)", class_name="Button").click_input()
    send_button = main_win.child_window(title="发送（1）", control_type="Button")
    send_button.click_input()


def list_files(directory, file_list,master_dict):
    """遍历目录，将文件路径和文件名添加到字典中，并将字典添加到列表中"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            match = re.search(r'_([^_]+)_', file)
            if match:
                sName = match.group(1)
            else:
                sName = ''  # 如果没有匹配到，设置一个默认值或进行其他处理
            file_path = os.path.join(root, file)
            file_dict = {'path': file_path, 'name': file,'searchName':sName,'groupName':master_dict.get(sName)}
            file_list.append(file_dict)

# 指定要遍历的目录
directory = 'C:\\Users\\guiyuan.zhang\\Desktop\\PMO'

# 创建一个空列表来存储所有文件的字典
files_array = []

#读取供应商对应关系
df = pd.read_excel('C:\\Users\\guiyuan.zhang\\Desktop\\供应商对应关系.xlsx', engine='openpyxl')

# 将每行数据转换为字典并存储到列表中
dict_list = df.to_dict(orient='records')

# 创建一个空的大字典来存储所有字典的第一个键值对
master_dict = {}

# 遍历字典列表
for data_dict in dict_list:
    key=data_dict.get('供应商名称')
    value=data_dict.get('群聊名称')
    master_dict[key] = value

# 调用函数
list_files(directory, files_array,master_dict)


# 打印结果
for file_dict in files_array:
    print(file_dict)
    if  file_dict['groupName'] != None:
        send_file(file_dict['groupName'],file_dict['path'],"江桂圆")