import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 时间范围
t_pre = np.linspace(0,2,100)
t_charge = np.linspace(2, 10, 400)
t_discharge = np.linspace(10, 18, 400)
t_late = np.linspace(18,20,100)


v_pre = 5 * np.exp(-t_pre - 6)

# 电容充电曲线
v_charge = 5 * (1 - np.exp(-t_charge + 2))

# 电容放电曲线
v_discharge = 5 * np.exp(-t_discharge + 10)


v_late = 5 * (1-np.exp(-t_late + 18))

custom_colors = sns.color_palette("RdBu", n_colors=10)
# 设置Seaborn样式
sns.set(style="whitegrid")
# 绘制图像
plt.figure(figsize=(10, 4))
plt.plot(t_pre, v_pre,color = custom_colors[0])
plt.plot(t_charge, v_charge, label='Charge',color=custom_colors[9])
plt.plot(t_discharge, v_discharge, label='Discharge',color = custom_colors[0])
plt.plot(t_late,v_late,color = custom_colors[9])


plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)
plt.grid(True, color='gray', linestyle='-', linewidth=0.5)
plt.gca().set_facecolor('#e9e9e9')
plt.tight_layout()
plt.legend()
plt.savefig('pic.png',dpi=300)
plt.show()

t = np.linspace(0, 20, 1000)

# 定义参数
R = 0.5
L = 1
C = 0.1
V0 = 1

# 计算电流
I = V0 / np.sqrt((L/C)) * np.exp(-R*t/(2*L)) * np.sin(np.sqrt((1/(L*C)) - (R**2 / (4*L**2))) * t)

# 绘制图像
plt.figure(figsize=(10, 6))
plt.plot(t, I, label='Current')
plt.xlabel('Time')
plt.ylabel('Current')
plt.title('Underdamped RLC Circuit')
plt.gca().set_facecolor('#e9e9e9')
plt.gca().axes.get_xaxis().set_visible(False)  # 隐藏 x 轴数字
plt.gca().axes.get_yaxis().set_visible(False)  # 隐藏 y 轴数字
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.savefig('pic-rlc.png',dpi=300)
plt.show()