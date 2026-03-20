import threading

from export import *
from WeChat import WeChat
from QQ import QQ
from getCoInfo import getCoInfo
from getSupplyInfo import getSupplyInfoAll
import time

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

wechat = WeChat()
qq = QQ()

#读取供应商全称信息
master_dict = getSupplyInfoAll()
#读取供应商简称信息
# master_dict = getSupplyInfo()

#读取PMO文件夹
files_array = getCoInfo(master_dict)

# 存储失败列表
failList=[]


# 记录开始时间
start_time = time.time()

for item in files_array:
    group = item['group']
    file_path = item['path']
    supplyName = item['searchName']

    # 当供应商关系表中查无供应商时跳出
    if master_dict.get(supplyName) is None:
        failList.append(item)
        continue

    groupName = group[0]
    purchaseName = str(group[3])
    planName = str(group[4])
    platform = group[1]

    # 当供应商关系表中查无群聊名称时跳出
    if groupName == 0:
        failList.append(item)
        continue

    msg = "你好，本周补货单，麻烦尽快安排，不足起订量请@"+planName+"{ENTER}沟通@"+purchaseName #+"{ENTER}"

    try:
        if platform == '微信' and groupName != 0:
            result = wechat.sendFile(file_path,groupName, msg)
        if platform == 'QQ' and groupName != 0:
            result = qq.sendFile(file_path,groupName, msg)
    except Exception as e:
        failList.append(item)
        continue

    print(groupName+": "+result)

    if result != "success":
        failList.append(item)
        continue

    result = ""
    # 发送完成后使用线程删除文件 线程中等待2秒防止文件发送失败
    delete_thread = DeleteFileThread(file_path)
    delete_thread.start()

if not failList:
    print("全部成功")
else:
    exportFile(failList,"失败文件")

    print("以下发送失败")
    for item in failList:
        print(item.get('searchName'), item.get('group'))


# 记录结束时间
end_time = time.time()

# 计算并打印执行时间
print(f"执行时间：{(end_time - start_time) / 60}分钟")


