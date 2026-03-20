import pandas as pd

# 指定Excel文件路径和工作表名称

def getSupplyInfo():
    supplyGroup = pd.read_excel('C:\\Users\\guiyuan.zhang\\Desktop\\供应商对应关系.xlsx', engine='openpyxl')
    # 将每行数据转换为字典并存储到列表中
    supplyGroup.fillna(0, inplace=True)
    supplyGroup_list = supplyGroup.to_dict(orient='records')
    # 创建一个空的大字典来存储所有供应商信息
    master_dict = {}
    # 遍历字典列表
    for data_dict in supplyGroup_list:
        key=data_dict.get('供应商简称')
        templist = []
        templist.append(data_dict.get('群聊名称'))
        templist.append(data_dict.get('平台'))
        templist.append(data_dict.get('备注'))
        templist.append(data_dict.get('采购负责人'))
        templist.append(data_dict.get('补货负责人'))
        value = templist
        master_dict[key] = value

    return master_dict


def getSupplyInfoAll():
    supplyGroup = pd.read_excel('C:\\Users\\guiyuan.zhang\\Desktop\\供应商对应关系.xlsx', engine='openpyxl')
    # 将每行数据转换为字典并存储到列表中
    supplyGroup.fillna(0, inplace=True)
    supplyGroup_list = supplyGroup.to_dict(orient='records')
    # 创建一个空的大字典来存储所有供应商信息
    master_dict = {}
    # 遍历字典列表
    for data_dict in supplyGroup_list:
        key=data_dict.get('供应商名称')
        templist = []
        templist.append(data_dict.get('群聊名称'))
        templist.append(data_dict.get('平台'))
        templist.append(data_dict.get('备注'))
        templist.append(data_dict.get('采购负责人'))
        templist.append(data_dict.get('补货负责人'))
        value = templist
        master_dict[key] = value

    return master_dict