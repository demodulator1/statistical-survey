import pandas as pd

# 读取 Excel 文件
file_path = '分析数据2.xls'  # 替换为你的文件路径
sheet_name = 'Sheet1'  # 替换为你的工作表名称

# 读取数据，使用 xlrd 引擎来处理 .xls 文件
df = pd.read_excel(file_path, sheet_name=sheet_name, engine='xlrd')

# 对每一列求和并添加到列的最后
sums = df.sum(numeric_only=True)  # 只对数值列求和
sums_df = pd.DataFrame(sums).T  # 将 Series 转换为 DataFrame
sums_df.index = ['Sum']  # 设置索引为 'Sum'

# 将结果添加到原数据框
df_with_sums = pd.concat([df, sums_df], ignore_index=True)

# 保存到新的 Excel 文件
output_file_path = 'output_with_sums.xlsx'  # 替换为你想保存的文件路径
df_with_sums.to_excel(output_file_path, index=False)

print(f"文件已保存到 {output_file_path}")
