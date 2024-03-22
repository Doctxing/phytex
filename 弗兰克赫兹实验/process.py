import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import find_peaks

data = pd.read_excel('mydata.xlsx')

data.info()

combine=0

x = data.iloc[:,0]
y1 = data.iloc[:,1]
y2 = data.iloc[:,2]
peaks_y1, _ = find_peaks(y1)
peaks_y2, _ = find_peaks(y2)

custom_colors = sns.color_palette("RdBu", n_colors=10)

# 设置Seaborn样式
sns.set(style="whitegrid")

if combine==0 :
    # 创建左侧图
    plt.figure(figsize=(16, 6))
    plt.subplot(1, 2, 1)
    sns.lineplot(x=x, y=y1,color=custom_colors[0])
    plt.scatter(x.iloc[peaks_y1], y1.iloc[peaks_y1], color=custom_colors[1],marker='^')  # 标记峰值
    for peak in peaks_y1:
        plt.vlines(x=x.iloc[peak],ymin=0,ymax=y1.iloc[peak], color=custom_colors[1], linestyle='--') # 在峰值处绘制竖直线
        plt.text(x.iloc[peak],-1,str(x.iloc[peak]),fontsize=12, color='black', ha='center', va='top')
    plt.xlabel(r'$U_{G2K}$')
    plt.ylabel(r'$I_A (nA)$')
    plt.title(r'$U_{G2A}=7.08V$')
    plt.gca().set_facecolor('#e9e9e9')

    # 创建右侧图
    plt.subplot(1, 2, 2)
    sns.lineplot(x=x, y=y2,color=custom_colors[9])
    plt.scatter(x.iloc[peaks_y2], y2.iloc[peaks_y2], color=custom_colors[8],marker='^')  # 标记峰值
    for peak in peaks_y2:
        plt.vlines(x=x.iloc[peak],ymin=0,ymax=y2.iloc[peak], color=custom_colors[8], linestyle='--') # 在峰值处绘制竖直线
        plt.text(x.iloc[peak],-1,str(x.iloc[peak]),fontsize=12, color='black', ha='center', va='top')
    plt.xlabel(r'$U_{G2K}$')
    plt.ylabel(r'$I_A (nA)$')
    plt.title(r'$U_{G2A}=7.58V$')
    plt.gca().set_facecolor('#e9e9e9')

    # 加入网格
    plt.grid(True)

    # 调整布局
    plt.tight_layout()

    plt.savefig('data-2.png',dpi=300)
    # 显示图形
    plt.show()
    
else:
    plt.figure(figsize=(10, 6))

    # 绘制第一个曲线及其峰值
    sns.lineplot(x=x, y=y1, color=custom_colors[0], label='$U_{G2A}=7.08V$')
    
    # 绘制第二个曲线及其峰值
    sns.lineplot(x=x, y=y2, color=custom_colors[9], label='$U_{G2A}=7.58V$')

    plt.xlabel(r'$U_{G2K}$')
    plt.ylabel(r'$I_A$ (nA)')
    plt.title('Frank-Hertz Experiment')
    plt.gca().set_facecolor('#e9e9e9')
    plt.legend()
    # 加入网格
    plt.grid(True)

    # 调整布局
    plt.tight_layout()

    plt.savefig('data.png',dpi=300)
    # 显示图形
    plt.show()