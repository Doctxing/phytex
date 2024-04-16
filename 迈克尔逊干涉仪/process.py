import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def least_squares_fit(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = np.sum(x**2)
    sum_xy = np.sum(x * y)
    
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    intercept = (sum_y - slope * sum_x) / n
    
    return slope, intercept

# 生成一些示例数据
x = np.array([0, 50, 100, 150, 200, 250])
y = np.array([0, 4.5, 8.8, 13.3, 17.7, 22.3])

# 最小二乘拟合
slope, intercept = least_squares_fit(x, y)

# 输出斜率和截距信息
print("斜率:", slope)
print("截距:", intercept)

custom_colors = sns.color_palette("RdBu", n_colors=10)
# 设置 Seaborn 样式和背景网格线
sns.set_style("whitegrid")

# 绘制原始数据和拟合直线
plt.figure(figsize=(16,6))
plt.scatter(x, y, color=custom_colors[0], label='Data points')
plt.plot(x, slope * x + intercept, color=custom_colors[0], label='Fitted line')
plt.xlabel(r'$\Delta P$')
plt.ylabel(r'$\Delta n$')
plt.gca().set_facecolor('#e9e9e9')
plt.legend()
plt.savefig('plot.png',dpi=300)
plt.show()
