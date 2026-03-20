import pandas as pd
from loadFile import *
from sendFile import *
from sendFileQQ import send_file_QQ

# 指定PMO的目录
directory = 'D:\\PMO-测试-1'

# 创建一个空列表来存储所有文件的字典
files_array = []

#读取供应商对应关系
df = pd.read_excel('C:\\Users\\guiyuan.zhang\\Desktop\\供应商对应关系.xlsx', engine='openpyxl')

# 将每行数据转换为字典并存储到列表中


dict_list = df.to_dict(orient='records')

print(dict_list)


for data in dict_list:
    # 获取供应商名称作为文件名
    filename = "测试_"+f"{data['供应商名称']}"+"_测试"+".xlsx"
    file_path = os.path.join(directory, filename)

    # 创建一个DataFrame
    df = pd.DataFrame([data])  # 将字典转换为DataFrame

    # 使用pandas的ExcelWriter，指定openpyxl为引擎
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)  # 写入数据到Excel文件

    print(f'文件 {filename} 已创建')