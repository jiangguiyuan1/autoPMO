import pandas as pd
from loadFile import *
from sendFile import *

# 指定PMO的目录
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
    templist = []
    templist.append(data_dict.get('群聊名称'))
    templist.append(data_dict.get('平台'))
    value=templist
    master_dict[key] = value

print(dict_list)
print(master_dict.get('广州亿路达贸易有限公司')[1])