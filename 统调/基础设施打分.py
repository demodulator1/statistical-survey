import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import re

# 设置中文字体
plt.rcParams['font.family'] = ['Microsoft YaHei']

# 读取 Excel 文件
file_path = '预处理后文件数据.xlsx'  # 替换为你的文件路径
df = pd.read_excel(file_path)

# 确保 Excel 文件中包含指定列
column_name = "24.您更希望能获得哪方面的公共服务保障?"
if column_name not in df.columns:
    raise ValueError(f"Excel 文件中没有找到列：{column_name}")

# 获取指定列的数据
data = df[column_name].dropna()  # 去掉缺失值

# 分词并统计服务类型出现次数
all_services = []
for entry in data:
    services = entry.split('┋')  # 根据分隔符分词
    all_services.extend(services)  # 将所有分词结果加入列表

# 使用 Counter 统计每种服务的出现次数
service_counts = Counter(all_services)

# 过滤出现次数大于100的服务
filtered_counts = {service: count for service, count in service_counts.items() if count > 100}

# 保留仅包含中文字符的服务
def filter_chinese(text):
    # 仅保留中文字符
    return ''.join(re.findall(r'[\u4e00-\u9fff]', text))

# 应用过滤函数
filtered_counts = {filter_chinese(service): count for service, count in filtered_counts.items() if filter_chinese(service)}

# 准备数据用于绘图
services = list(filtered_counts.keys())
counts = list(filtered_counts.values())

# 绘制柱状图
plt.figure(figsize=(12, 8))  # 设置图形大小
bars = plt.bar(services, counts, color='#66b3ff')  # 设置统一颜色

# 在柱形图上显示数值
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}', ha='center', va='bottom')

# 设置坐标轴和标题
plt.xlabel('服务类型')
plt.ylabel('出现次数')
plt.title('公共服务需求统计')

# 旋转横坐标标签
plt.xticks(rotation=45, ha='right')

# 自动调整布局以防止标签被遮挡
plt.tight_layout()

# 显示图形
plt.show()
