import re
from collections import Counter

import pandas as pd
from export import *
from getSupplyInfo import getSupplyInfo
from sendCoQQ import send_co_QQ
from sendCoWX import send_co_WX
from sendCoWX_V2 import send_co_WX_V2
from DD import *
from processManger import *
import sys

# 检查QQ窗口数量
code = check_QQ()
if code !='success':
    print("程序中断：找到两个或更多的 'QQ' 窗口")
    sys.exit(1)

#读取供应商信息
master_dict = getSupplyInfo()

#读取未结单明细
file_path = r"C:\Users\guiyuan.zhang\Desktop\未结单明细表3.19.xlsx"
sheet_name = '明细'
# 使用openpyxl引擎读取指定工作表
planList = ['黄峥','刘乐婷','李远翘','陈伟锡','杨骏榔','黄青兰','林舒影','邓颖焰','张桂源','袁梓清']
statusList = ['少货','未到货']
#planList = ['张桂源']
df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl',header=1)
df.fillna(0, inplace=True)
filter_df = df[(df['SKU入库状态'].isin(statusList))
                #&(df['首次接收日期']==0)
                &(df['采购类型']=='补货') #26/02/05
                &(df['是否可以入库']=='可入库') #26/02/05
                #&(df['是否超期']=='超期') 26/02/05
                &(df['跟进人']!='梁晓霞')]
                #&(df['SKU信息 → 补货负责人'].isin(planList))]

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
    # status = item.get("SKU入库状态")
    # if status == "少货":
    #     co_List = [SKU, " 欠货" + str(Num) + "件，没来货"]
    # if status == "未到货":
    #     co_List = [SKU," 订货"+str(Num)+"件，没来货"]
    co_List = [SKU, " 欠货" + str(Num) + "件，没来货"]
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

count = len(supply_dict)
send_count = 0

for key,value in supply_dict.items():
    send_count = send_count + 1
    result = ""
    string = str(value)
    string = re.sub(r'[\[\]{},\']', '', string)
    # string = re.sub(r':', ':^{ENTER}', string)
    string = re.sub(r'C', '\nC', string)
    string = re.sub(r'a', '\na', string)
    string = string+"\n如有退款，可忽略已退款项"
    charLength = len(string)

    if master_dict.get(key) == None:
        failList.append({'供应商':key,'催货明细':string,'失败原因':"无供应商信息",'供应商对应关系':""})
        continue

    supplyInfo = master_dict[key]
    group = supplyInfo[0]
    platform = supplyInfo[1]
    planName = supplyInfo[4]

    if charLength>4000 and platform == 'QQ':
        failList.append({'供应商': key, '催货明细': string, '失败原因': "字数过多", '供应商对应关系': supplyInfo})
        continue
    if charLength>1900 and platform == '微信':
        failList.append({'供应商': key, '催货明细': string, '失败原因': "字数过多", '供应商对应关系': supplyInfo})
        continue
    if platform == 0:
        failList.append({'供应商':key,'催货明细':string,'失败原因':"无供应商信息",'供应商对应关系':supplyInfo})
        continue
    try:
        if platform == 'QQ':
            result = send_co_QQ(group,string,"",planName)
        if platform == '微信':
            #3.9版本
            #result = send_co_WX(group, string,"",planName)
            #4.1版本
            result = send_co_WX_V2(group, string,"",planName)
        if result != 'success':
            failList.append({'供应商':key,'催货明细':string,'失败原因':result,'供应商对应关系':supplyInfo})
            print(result,supplyInfo)
    except Exception as e:
        failList.append({'供应商':key,'催货明细':string,'失败原因':result,'供应商对应关系':supplyInfo})
        continue

    print(send_count, "/", count)

if not failList :
    print("全部成功")
else:
    full_file_path = exportFile(failList, "失败文件")
    print("以下发送失败")
    for item in failList:
        print(item)
    # 发送失败文件
    # dd = DD()
    # dd.search("库存-采购内部沟通群")
    # dd.sendFile(full_file_path)