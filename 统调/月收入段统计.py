import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('预处理后文件数据.xlsx')

age_column = '您的月收入状况？'

# 统计数量
age_counts = df[age_column].value_counts()
total_count = age_counts.sum()

# 计算占比
age_percentages = age_counts / total_count * 100

# 输出结果
print(f"总人数: {total_count}")
for age_group, count in age_counts.items():
    print(f"{age_group}的数量: {count}")
    print(f"{age_group}的占比: {age_percentages[age_group]:.2f}%")
