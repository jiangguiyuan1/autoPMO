import re
from collections import Counter

import pandas as pd
from export import *


path = r"D:\webdownload\查询结果 - 2025-04-10T110603.903.csv"

df = pd.read_csv(path)

target_skus = [
    'a23102600ux0176',
    'a23111600ux0308',
    'a22122800ux0002',
    'a22122700ux0145',
    'a24010400ux0027',
    'a22122700ux0145',
    'a23061200ux0065',
    'a23102700ux0211',
    'a22122800ux0002',
    'a23111600ux0313',
    'a23072500ux0389',
    'a23082500ux0271',
    'a22012000ux0524',
    'a20102800ux0480',
    'a23090600ux0476',
    'a23030600ux0014',
    'a22032100ux0034',
    'a23081800ux0129',
    'a22090100ux0462',
    'a23111700ux0127',
    'a23101700ux0608',
    'a23083100ux0388',
    'a23103000ux0270',
    'a22072500ux0551',
    'a22103000ux0097',
    'a22011700ux0082',
    'a23081800ux0128',
    'a23081500ux0607',
    'a24011700ux0244'
]

# 筛选特定的 SKU
filtered_df = df[df['sku'].isin(target_skus)]

# 将结果导出到桌面
desktop_path = os.path.expanduser('~/Desktop')
output_file_path = os.path.join(desktop_path, 'filtered_results.csv')
filtered_df.to_csv(output_file_path, index=False)

print(f"筛选后的数据已导出到: {output_file_path}")