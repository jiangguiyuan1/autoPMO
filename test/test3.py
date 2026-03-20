import re

import pandas as pd

from getSupplyInfo import getSupplyInfo
from sendCoQQ import send_co_QQ
from sendCoWX import send_co_WX

#读取供应商信息
master_dict = getSupplyInfo()

#读取未结单明细
file_path = "C:\\Users\\guiyuan.zhang\\Desktop\\未结单明细表1025.xlsx"
sheet_name = '明细'
# 使用openpyxl引擎读取指定工作表
#planList = ['黄峥','刘乐婷','李远翘','陈伟锡','杨骏榔','黄青兰','林舒影','邓颖焰','张桂源']
planList = ['张桂源']
df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl',header=1)
df.fillna(0, inplace=True)
filter_df = df[(df['采购类型']=='补货')
                &(df['首次接收日期']==0)
                &(df['SKU入库状态']=='未到货')
                &(df['是否可以入库']=='可入库')
                &(df['是否超期']=='超期')
                &(df['补货负责人'].isin(planList))]

dict_list = filter_df.to_dict(orient='records')
supply_dict = {}
co_Dict = {}


# 动态添加字典
def add_dict(main_dict, key, sub_dict):
    main_dict[key] = sub_dict
# 生成催单明细字典
for item in dict_list:
    supplyName = item.get("工厂简称")
    CO = item.get("补货单号")
    SKU = item.get("SKU信息")
    Num = item.get("未入库件数")
    co_List = [SKU,Num]
    #co_Dict[CO] = {co_List}
    supply = supply_dict.get(supplyName)
    if supply is None:
        supply_dict[supplyName] = {CO:[co_List]}
    if supply is not None:
        co = supply_dict[supplyName].get(CO)
        if co is None :
            add_dict(supply_dict[supplyName],CO,[co_List])
        if co is not None :
            co.append(co_List)

#print(master_dict)
# 存储失败列表
failList=[]

for key,value in supply_dict.items():

    if master_dict.get(key) == None:
        failList.append({key: value})
        continue

    supplyInfo = master_dict[key]
    group = supplyInfo[0]
    platform = supplyInfo[1]
    planName = supplyInfo[4]
    #print(group,platform,planName)
    #print(value)
    string = str(value)
    string = re.sub(r'[\[\]{},\']', '', string)
    #string = re.sub(r':', ':^{ENTER}', string)
    string = re.sub(r'C', '\nC', string)
    string = re.sub(r'a', '\na', string)
    print(string)