import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('预处理后文件数据.xlsx')

# 假设“您的性别：”列的名称为 '性别'
gender_column = '性别'

# 统计数量
gender_counts = df[gender_column].value_counts()
total_count = gender_counts.sum()

# 计算占比
gender_percentages = gender_counts / total_count * 100

# 输出结果
print(f"总人数: {total_count}")
print(f"男的数量: {gender_counts.get('男', 0)}")
print(f"女的数量: {gender_counts.get('女', 0)}")
print(f"男的占比: {gender_percentages.get('男', 0):.2f}%")
print(f"女的占比: {gender_percentages.get('女', 0):.2f}%")
