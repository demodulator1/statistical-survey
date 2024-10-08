import pandas as pd
import numpy as np
from factor_analyzer import calculate_kmo
# 读取Excel文件
df = pd.read_excel('效度分析.xlsx')
# 如果需要选择特定列，请在这里修改
data = df.copy()
# 去除任何非数值列（如果有的话）
data = data.select_dtypes(include=[np.number])
# 计算相关矩阵
correlation_matrix = data.corr()
# 计算KMO值
kmo_all, kmo_model = calculate_kmo(correlation_matrix)
print(f"KMO值为: {kmo_model}")
