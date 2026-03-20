import pandas as pd

# 读取两份 Excel 文件
file1 = r"C:\Users\guiyuan.zhang\Desktop\价格表.xlsx"  # 第一份 Excel 文件路径
file2 = r"C:\Users\guiyuan.zhang\Desktop\账号主仓关系表.xlsx"  # 第二份 Excel 文件路径

# 读取数据
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# 通过 pid 字段进行匹配合并（左连接）
merged_df = pd.merge(df1, df2, on=''and '' , how='left')

# 选择需要保留的字段
# 假设你需要保留的字段是 df1 中的 'field1', 'field2' 和 df2 中的 'field3', 'field4'
#selected_columns = ['pid', 'field1', 'field2', 'field3', 'field4']
#final_df = merged_df[selected_columns]

# 保存结果到新的 Excel 文件
output_file = 'merged_data_left_all.xlsx'
merged_df.to_excel(output_file, index=False)

print(f"数据已成功合并并保存到 {output_file}")