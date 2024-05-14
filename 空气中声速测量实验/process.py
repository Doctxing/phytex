import numpy as np
import pandas as pd 

data = pd.read_csv("./空气中声速测量实验/data.csv")
f = 37.042
t = 22.7
meth_line = [data['0'],data['1'],data['2']]
timemeth_lenth = data["li"]
timemeth_line = data['3']
Type = data['type']
Type_lenth = data['l2']
Type_time = data['time']
v0 = 331.45*np.sqrt(1+t/273.15)

print("v = "+str(v0))
for i in range(0,3):
    temp = 0
    for j in range(0,5):
        temp += (meth_line[i].iloc[j+5]-meth_line[i].iloc[j])
    if (i == 2):
        temp /= (5*5)
    else:
        temp /= (5*2.5)
    print("\lamda = "+str(temp))
    print("v = "+str(temp*f))
    print("\delta = "+ str(np.abs(v0-temp*f)/v0)+"\n")

v_byv = 0
t_sum = 0
for i in range(0,5):
    v_byv += (timemeth_lenth.iloc[i+5]-timemeth_lenth.iloc[i])/(5*(timemeth_line.iloc[i+5]-timemeth_line.iloc[i]))
    t_sum += (timemeth_line.iloc[i+5]-timemeth_line.iloc[i])
print(v_byv*1000)
print(str(np.abs(v0-v_byv*1000)/v0)+"\n")
print((10*5*5)*1000/t_sum)
print(str(np.abs(v0-(10*5*5)*1000/t_sum)/v0)+"\n")

v=[[],[]]
for i in range(0,2):
    v[0].append((Type_lenth[i+1]-Type_lenth[i])/(Type_time[i+1]-Type_time[i]))
    v[1].append((Type_lenth[i+1+3]-Type_lenth[i+3])/(Type_time[i+1+3]-Type_time[i+3]))

for i in range(0,2):
    print(v[i][0])
    print(v[i][1])
    print(str((v[i][1]+v[i][0])/2)+'\n')