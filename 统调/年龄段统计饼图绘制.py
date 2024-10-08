import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 设置中文字体
plt.rcParams['font.family'] = ['Microsoft YaHei']

# 数据
labels = ['18岁以下', '18岁～30岁', '31岁～40岁', '41岁～50岁', '60岁以上']
sizes = [0.18, 25.31, 36.28, 22.83, 5.31]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# 计算每个扇区的角度
angles = np.array(sizes) / sum(sizes) * 360
angles = np.concatenate(([0], np.cumsum(angles)))

# 创建图形
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制每个扇区
for i in range(len(labels)):
    # 计算每个扇区的中心点
    theta = np.linspace(np.radians(angles[i]), np.radians(angles[i+1]), 100)
    x = np.cos(theta)
    y = np.sin(theta)
    z = np.zeros_like(x)

    # 为每个扇区创建多边形
    x = np.concatenate(([0], x))
    y = np.concatenate(([0], y))
    z = np.concatenate(([0], z))

    verts = [list(zip(x, y, z))]
    poly3d = Poly3DCollection(verts, color=colors[i], alpha=0.6)
    ax.add_collection3d(poly3d)

# 设置标签和标题
ax.set_title('年龄分布三维饼图')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# 显示图例
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, labels, loc='upper right')

plt.show()
