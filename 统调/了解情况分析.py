import pandas as pd

# 读取 Excel 文件
file_path = '预处理后文件数据.xlsx'  # 替换为你的文件路径
df = pd.read_excel(file_path)

# 假设列名为 "您对本地基础设施建设的完善程度了解吗？"
column_name = "您对本地基础设施建设的完善程度了解吗？"

# 统计各值的出现次数
value_counts = df[column_name].value_counts()

# 计算占比
total_count = len(df)
percentages = (value_counts / total_count) * 100

# 将结果合并到一个 DataFrame 中
result = pd.DataFrame({
    '值': value_counts.index,
    '人数': value_counts.values,
    '占比 (%)': percentages.values
})

# 输出结果
print(result)

# 如果需要将结果保存为新的 Excel 文件
result.to_excel('output_statistics.xlsx', index=False)
