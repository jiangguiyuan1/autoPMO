import pandas as pd
from loadFile import *
from sendFile import *
from sendFileQQ import send_file_QQ
import numpy as np

# 指定PMO的目录
directory = 'D:\\PMO-派单'

# 创建一个空列表来存储所有文件的字典

files_array = []

#读取供应商对应关系
df = pd.read_excel('C:\\Users\\guiyuan.zhang\\Desktop\\供应商对应关系.xlsx', engine='openpyxl')

# 将每行数据转换为字典并存储到列表中

df.fillna(0, inplace=True)
dict_list = df.to_dict(orient='records')

# 创建一个空的大字典来存储所有字典的第一个键值对
master_dict = {}

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

# 调用函数
list_files(directory, files_array,master_dict)

# 发送失败列表
failList=[]

# 打印结果
for file_dict in files_array:

    supplyName = file_dict['searchName']
    # 当供应商关系表中查无供应商时跳出
    if master_dict.get(supplyName) is None:
        failList.append(file_dict)
        continue

    group = file_dict['group']
    # print(file_dict)
    if  group[0] == 0 :
        s=file_dict.get('name')
        match = re.search(r'_([^_]+)_', s)
        print(match.group(1),group[2],group[3],group[4])
    # s = file_dict.get('name')
    # match = re.search(r'_([^_]+)_', s)
    # print(match.group(1), group[2], group[3], group[4])