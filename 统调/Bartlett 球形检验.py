import pandas as pd
import numpy as np
from scipy import stats

# 读取Excel文件
df = pd.read_excel('效度分析.xlsx')

# 假设要分析的列在DataFrame的所有列中
data = df.copy()

# 去除任何非数值列（如果有的话）
data = data.select_dtypes(include=[np.number])

# 计算相关矩阵
correlation_matrix = data.corr()

# 对角线元素加上小的常数以避免行列式为0
epsilon = 1e-8
adjusted_matrix = correlation_matrix + np.eye(correlation_matrix.shape[0]) * epsilon

# 计算调整后的相关矩阵的行列式
det_cov = np.linalg.det(adjusted_matrix)

# 获取数据的样本数和变量数
n, p = data.shape

# 计算 Bartlett 的统计量
chi2_statistic = - (n - 1 - (2 * p + 5) / 6) * np.log(det_cov)

# 计算自由度
df = p * (p - 1) / 2

# 计算 p 值
p_value = 1 - stats.chi2.cdf(chi2_statistic, df)

print(f"近似卡方值: {chi2_statistic:.2f}")
print(f"自由度: {df:.0f}")
print(f"显著性: {p_value:.4f}")

if p_value < 0.05:
    print("相关矩阵不是单位矩阵，Bartlett检验建议因子分析可能是合适的。")
else:
    print("相关矩阵可能是单位矩阵，Bartlett检验建议因子分析可能不适合。")
