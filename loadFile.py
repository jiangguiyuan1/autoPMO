import os
import re


def list_files(directory, file_list,master_dict):
    """遍历目录，将文件路径和文件名添加到字典中，并将字典添加到列表中"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            match = re.search(r'_([^_]+)_', file)
            if match:
                sName = match.group(1)
            else:
                sName = ''  # 如果没有匹配到，设置一个默认值或进行其他处理

            file_path = os.path.join(root, file)
            file_dict = {'path': file_path, 'name': file,'searchName':sName,'group':master_dict.get(sName)}
            file_list.append(file_dict)






