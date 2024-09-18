import numpy as np
l01 = 45
l02 = 34
data = [[161,164.1,170.6,178.6,188],[26.1,21.0,30.1,26.0,26.5],[10,8,11,9,9]]
re = [[],[]]
for i in range(5):
    re[0].append(-data[1][i] * 10/data[2][i])
    re[1].append(-(250*data[0][i])/(l01*l02))
for i in range(5):
    print(round(re[0][i],3),'&',end='')
print('\n')
for i in range(5):
    print(round(re[1][i],3),'&',end='')