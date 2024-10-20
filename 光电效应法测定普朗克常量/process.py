import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import seaborn as sns

eee = 1.6e6

hhh = 6.626e5

data = [[8.213,7.402,6.876,5.491,5.196],
        [1.768,1.301,1.111,0.591,0.511],
        [1.796,1.375,1.195,0.619,0.558],
        [1.804,1.407,1.207,0.641,0.574]] 

colorset = sns.color_palette("RdBu", 10)
data = np.array(data)
for i in range(3):
    slope, intercept = np.polyfit(data[0], data[i+1], 1)
    m2 = slope*eee
    pltpp = (data[i+1][0]-data[i+1][-1])/(data[0][0]-data[0][-1])*eee
    print(f"Slope for dataset {i+1}, m2:{round(m2,3)},error:{round(np.abs(m2-hhh)/hhh*100,3)}%,fit:{round(pltpp,3)},error:{round(np.abs(pltpp-hhh)/hhh*100,3)}%")
    plt.plot(data[0], data[i+1], label=f"Raw Data", color=colorset[9],marker='o')
    plt.plot(data[0], slope*data[0]+intercept, label=f"Fitted line",color = colorset[0])
    plt.xlabel(r"$\nu/\times 10^{14} Hz$")
    plt.ylabel(r"$U_c/V$")
    plt.title("Photoelectric effect line "+rf"$(l = {2**(i+1)} mm )$")
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.savefig(f"l_{2**(i+1)}.png",dpi=300)
    plt.show()
    