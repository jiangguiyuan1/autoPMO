from loadFile import list_files


# 指定PMO的目录
def getCoInfo(master_dict):
    directory = 'D:\\PMO-派单'

    # 创建一个空列表来存储所有文件的字典
    files_array = []

    # 读取派单目录
    list_files(directory, files_array,master_dict)

    return files_array