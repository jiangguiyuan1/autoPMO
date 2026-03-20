import os

import pandas as pd
from pandas import notnull

from inviteQQGroup import invite_QQ
from inviteWXGroup import invite_WX

#读取供应商对应关系
df = pd.read_excel('C:\\Users\\guiyuan.zhang\\Desktop\\供应商对应关系.xlsx', engine='openpyxl')
apply = pd.read_excel('C:\\Users\\guiyuan.zhang\\Desktop\\拉群.xlsx', engine='openpyxl')

df.fillna(0, inplace=True)
applyList = apply.to_dict(orient='records')
supplyList = df.to_dict(orient='records')



# 创建一个空的大字典来存储所有字典的第一个键值对
master_supply_dict = {}

# 遍历字典列表
for supply_dict in supplyList:
    key=supply_dict.get('供应商简称')
    templist = []
    templist.append(supply_dict.get('群聊名称'))
    templist.append(supply_dict.get('平台'))
    master_supply_dict[key] = templist

# 存储失败列表
failList=[]


for item in applyList:
    supplyName = item['供应商名称']
    applyName = item['申请人']
    #print(supplyName,applyName)
    if master_supply_dict.get(supplyName) == None:
        failList.append(item)
        continue
    groupName = master_supply_dict.get(supplyName)[0]
    platForm = master_supply_dict.get(supplyName)[1]
    #print(groupName,platForm)
    try:
        if platForm == "QQ" and groupName != 0 :
            result = invite_QQ(groupName, applyName)
        if platForm == "微信" and groupName != 0:
            result = invite_WX(groupName, applyName)
    except Exception as e:
        failList.append(item)

    print(result)

    if result != "success":
        failList.append(item)

    result = ""

if not failList :
    print("全部成功")
else:
    print("以下添加失败")
    for item in failList:
        print(item)
