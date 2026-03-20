import json
import pandas as pd

# 假设你的 JS 文件内容保存在 data.js 中
js_file_path = 'data.js'

# 读取 JS 文件内容
with open(js_file_path, 'r', encoding='utf-8') as file:
    js_content = file.read()

# 提取 JSON 数据部分
start_marker = "module.exports="
if start_marker in js_content:
    json_data = js_content.split(start_marker, 1)[1]
else:
    raise ValueError("无法找到 JSON 数据部分")

# 解析 JSON 数据
data = json.loads(json_data)

# 创建一个空的列表来存储整理后的数据
result = []

# 遍历省份
for province_code, province_name in data.get("86", {}).items():
    # 遍历省份下的城市
    for city_code, city_name in data.get(province_code, {}).items():
        # 遍历城市下的区县
        for district_code, district_name in data.get(city_code, {}).items():
            result.append([province_name, city_name, district_name])

# 将结果转换为 DataFrame
df = pd.DataFrame(result, columns=['省', '市', '区'])

# 保存为 Excel 文件
excel_file_path = 'output.xlsx'
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f"数据已成功导出到 {excel_file_path}")