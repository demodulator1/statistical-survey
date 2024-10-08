import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.family'] = ['Microsoft YaHei']

# 数据
categories = ['＜1000元', '1000~2000元', '2000~5000元', '＞5000元']
values = [2.12, 4.60, 54.16, 39.12]
colors = ['#66b3ff'] * len(categories)  # 所有柱子都用相同的蓝色

# 绘制柱状图
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=colors)

# 在柱状图上显示占比数字
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}%',
             ha='center', va='bottom')

plt.xlabel('收入区间')
plt.ylabel('占比 (%)')
plt.title('收入分布柱状图')
plt.ylim(0, 60)  # 设定 y 轴范围以适应数据
plt.show()
