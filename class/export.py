import os

import pandas as pd

def exportFile(failList,fileName):
    failInfo = pd.DataFrame(failList)
    # 获取桌面路径
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Windows
    date_str = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
    file_name = fileName
    file_format = 'xlsx'  # 文件格式
    # 完整的文件名，包含格式和时间戳
    full_file_name = f"{file_name}_{date_str}.{file_format}"
    # 完整的文件路径
    full_file_path = os.path.join(desktop_path, full_file_name)
    # 将DataFrame写入Excel文件
    failInfo.to_excel(full_file_path, index=False, engine='openpyxl')  # 使用openpyxl作为引擎