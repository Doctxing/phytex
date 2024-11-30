import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

raw_error = -0.003
raw_data = np.array([
            [30,35,40,45,50,55],
            [0.999,0.991,0.992,1.001,1.005,1.000],                                                   
            [29.19,19.23,14.32,10.52,7.69,5.94]
])

rho = 7800
rho_0 = 950
g = 9.8
dd = 0.02
ll = 0.2
raw_data[1] = (raw_data[1] - raw_error)*1e-3
d_mean = np.mean(raw_data[1])
S_d = np.sqrt(np.sum((raw_data[1]-d_mean)**2)/30)
print("S_d = ",round(S_d*1e3,3),"mm")
u_1 = 0.01/np.sqrt(3)*1e-3
u_d = np.sqrt(S_d**2+u_1**2)
print("u_d = ",round(u_d*1e3,3),"mm")
u_t = 0.2/np.sqrt(3)
E_eta = np.sqrt(u_t**2/raw_data[2]**2+u_d**2 * (2/raw_data[1]-2.4/(dd+2.4*raw_data[1]))**2)
ovl_eta = (rho-rho_0)*g*raw_data[1]**2*raw_data[2]/(18*ll*(1+2.4*raw_data[1]/dd))
u_eta = E_eta*ovl_eta
df_out = pd.DataFrame({
    "T":raw_data[0].round(0),
    "eta":ovl_eta.round(3),
    "u_eta":u_eta.round(3),
    "E_eta":(E_eta*100).round(2)
})

print(df_out)

plt.errorbar(df_out["T"], df_out["eta"], yerr=df_out["u_eta"], capsize=5, label='Data with uncertainty')
plt.xlabel('Temperature (T)')
plt.ylabel('Viscosity (eta)')
plt.title('Viscosity vs Temperature')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('vscsty_vs_tmprtr.png',dpi=300)
#plt.show()