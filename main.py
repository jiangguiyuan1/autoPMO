import os
import time
import pandas as pd
from loadFile import *
from sendFile import *
from sendFileQQ import send_file_QQ
from sendFileTim import send_file_TIM
from wx_sendCo import send_file_WX
import threading
import random
from DD import *
from export import *
from processManger import *
import sys

def delete_file(file_path):
    if os.path.exists(file_path):
        try:
            time.sleep(2)
            os.remove(file_path)
            print(f"文件 {file_path} 已发送完成并删除")
        except Exception as e:
            print(f"删除文件 {file_path} 时出错: {e}")
    else:
        print(f"文件 {file_path} 不存在")

# 定义一个线程类来删除文件
class DeleteFileThread(threading.Thread):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        delete_file(self.file_path)

# 检查QQ窗口数量
code = check_QQ()
if code !='success':
    print("程序中断：找到两个或更多的 'QQ' 窗口")
    sys.exit(1)

# 指定PMO的目录
directory = 'D:\\PMO-派单'
#directory = 'D:\\PMO-测试-1'

# 创建一个空列表来存储所有文件的字典
files_array = []

#读取供应商对应关系
df = pd.read_excel('C:\\Users\\guiyuan.zhang\\Desktop\\供应商对应关系.xlsx', engine='openpyxl')
#df = pd.read_excel('C:\\Users\\guiyuan.zhang\\Desktop\\供应商对应关系-1.xlsx', engine='openpyxl')

# 将每行数据转换为字典并存储到列表中
df.fillna(0, inplace=True)
dict_list = df.to_dict(orient='records')

# 创建一个空的大字典来存储所有字典的第一个键值对
master_dict= {}

# 遍历字典列表
for data_dict in dict_list:
    key=data_dict.get('供应商名称')
    templist = []
    templist.append(data_dict.get('群聊名称'))
    templist.append(data_dict.get('平台'))
    templist.append(data_dict.get('备注'))
    templist.append(data_dict.get('采购负责人'))
    templist.append(data_dict.get('补货负责人'))
    value = templist
    master_dict[key] = value

# 读取派单目录
list_files(directory, files_array,master_dict)

# 存储失败列表
failList=[]

# 打乱 list 的顺序
random.shuffle(files_array)
# 记录开始时间
start_time = time.time()
count = len(files_array)
send_count = 0

for file_dict in files_array:
    group = file_dict['group']
    file_path = file_dict['path']
    supplyName = file_dict['searchName']

    send_count = send_count +1

    # 当供应商关系表中查无供应商时跳出
    if master_dict.get(supplyName) is None:
        failList.append(file_dict)
        continue

    # 当供应商关系表中查无群聊名称时跳出
    if group[0] == 0:
        failList.append(file_dict)
        continue
    result=""
    groupName = group[0]
    purchaseName = str(group[3])
    planName = group[4]
    #print(file_dict)
    #开始派单
    try:
        if group[1] == '微信' and groupName != 0:
            # 3.9.12.55版本
            # result = send_file(groupName,file_dict['path'],purchaseName,planName)
            # 4.1版本
            result =send_file_WX(groupName,file_dict['path'],purchaseName,planName)
        if group[1] == 'QQ' and groupName != 0:
            result = send_file_TIM(groupName,file_dict['path'],purchaseName,planName)
    except Exception as e:
        failList.append(file_dict)

    print(groupName+": "+result)

    if result != "success":
        failList.append(file_dict)
        continue

    #print(file_path)
    print(send_count,"/",count)
    #result =""
    # 发送完成后使用线程删除文件 线程中等待2秒防止文件发送失败
    delete_thread = DeleteFileThread(file_path)
    delete_thread.daemon = True  # 主线程退出时强制带走
    delete_thread.start()


if not failList :
    print("全部成功")
else:
    # failInfo = pd.DataFrame(failList)
    # failInfo.sort_values(by='path', inplace=True)
    # # 获取桌面路径
    # desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Windows
    # date_str = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
    # file_name = "失败文件"
    # file_format = 'xlsx'  # 文件格式
    # # 完整的文件名，包含格式和时间戳
    # full_file_name = f"{file_name}_{date_str}.{file_format}"
    # # 完整的文件路径
    # full_file_path = os.path.join(desktop_path, full_file_name)
    # # 将DataFrame写入Excel文件
    # failInfo.to_excel(full_file_path, index=False, engine='openpyxl')  # 使用openpyxl作为引擎

    full_file_path = exportFile(failList, "失败文件")
    print("以下发送失败")
    for item in failList:
        print(item.get('searchName'),item.get('group'))


    # 发送失败文件
    # dd = DD()
    # dd.search("相亲相爱一家人")
    # dd.sendFile(full_file_path)

# 记录结束时间
end_time = time.time()

# 计算并打印执行时间
print(f"执行时间：{(end_time - start_time) / 60}分钟")




