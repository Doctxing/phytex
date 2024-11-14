import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

colors1 = sns.color_palette("BrBG", 10)
colors2 = sns.color_palette("RdBu", 10)

colors_tobe_changed = [colors2[0],colors2[9]]

data = pd.read_csv('rawdata.csv')

lamdalist = [365.48,404.66,435.84,546.07,576.96,579.07]

x_data = data['位置(pixel)'].values
y_data = data['相对强度'].values

peaks = [1026,1239,1414,2028,2209]
fFWHM = np.array([111.35,73.812,84.793,75.74,88.422])

print(x_data[peaks])

k= (lamdalist[3]-lamdalist[2])/(x_data[peaks[3]]-x_data[peaks[2]])

b = lamdalist[2]-k*x_data[peaks[2]]

print('k=',round(k,2),'b=',round(b,2))

new_x = x_data*k+b

new_peaks = new_x[peaks]

print(new_peaks.round(2))
print(fFWHM*k)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 4))

plt.plot(new_x, y_data, label='Data', color=colors_tobe_changed[1])
plt.scatter(new_peaks, y_data[peaks], marker='x', label='Peaks', color=colors_tobe_changed[0])
for i, peak in enumerate(new_peaks):
    if i == 3:
        plt.text(peak + 35, y_data[peaks[i]] - 600, r'$\lambda = $'+f'{new_peaks[i]:.2f}', color=colors_tobe_changed[0], ha='center')
        plt.text(peak + 35, y_data[peaks[i]] - 1300, f'FWHM={fFWHM[i]:.2f}', color=colors_tobe_changed[0], ha='center')
    else:
        plt.text(peak, y_data[peaks[i]] + 1000, r'$\lambda = $'+f'{new_peaks[i]:.2f}', color=colors_tobe_changed[0], ha='center')
        plt.text(peak, y_data[peaks[i]] + 200, f'FWHM={fFWHM[i]*k:.2f}', color=colors_tobe_changed[0], ha='center')
plt.xlabel(r"$\lambda (nm) $")
plt.ylabel("强度")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('result.png',dpi=300)
plt.show()