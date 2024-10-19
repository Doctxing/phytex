import numpy as np
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data1 = [[-7,-6,-5,-4,-3,-2,-1,0,0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.7,3.0],
         [-0.189,-0.141,-0.1,-0.071,-0.048,-0.023,-0.012,0,0.006,0.02,0.053,0.128,0.267,0.576,1.205,3.1,11.9,58.5],
         [-0.315,-0.253,-0.2,-0.154,-0.109,-0.069,-0.033,0,0.01,0.019,0.03,0.042,0.055,0.072,0.098,0.167,0.449,1.342]]

data2 = [[793,411,248,169.5,124.4,96.5,77.2,63.8],
         [[3,2.91,2.84,2.78,2.73,2.68,2.64,2.60],
          [109.1,57.3,34.9,23.8,17.4,13.4,10.7,8.7]],
         [[3.05,2.96,2.88,2.82,2.76,2.72,2.68,2.64],
          [8.3,4.5,2.8,1.920,1.419,1.105,0.902,0.756]]]

data3 = [[0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8],
         [13.6,13.5,13.5,13.5,13.5,13.5,13.5,13.4,13.3,13.1,12.7,11.9,9.9,4.4,0],
         [1.125,1.115,1.090,1.077,1.071,1.058,1.034,1.014,0.982,0.939,0.885,0.798,0.642,0.343,0]]

colorset = sns.color_palette('RdBu',10)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.plot(data1[0], data1[1], label='Single-crystal silicon', marker='o',color = colorset[9])
ax1.set_xlabel('Voltage (V)')
ax1.set_ylabel('Current (mA)')
ax1.set_title('I-V Characteristics of Single-crystal Silicon')
ax1.legend()
ax1.grid(True)

ax2.plot(data1[0], data1[2], label='Amorphous silicon', marker='x',color = colorset[0])
ax2.set_xlabel('Voltage (V)')
ax2.set_ylabel('Current (mA)')
ax2.set_title('I-V Characteristics of Amorphous Silicon')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('1.png',dpi = 300)
#plt.show()

for i in range(2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    ax1.plot(data2[0], data2[i+1][0], label='Open-circuit voltage', marker='o',color = colorset[9])
    ax1.set_xlabel(r'Irradiance ($W/cm^2$)')
    ax1.set_ylabel('Voltage (V)')
    ax1.set_title('Open-Circuit Voltage vs. Light Intensity')
    ax1.legend()
    ax1.grid(True)
    
    ax2.plot(data2[0], data2[i+1][1], label='Short-circuit current', marker='x',color = colorset[0])
    ax2.set_xlabel(r'Irradiance ($W/cm^2$)')
    ax2.set_ylabel('Current (mA)')
    ax2.set_title('Short-Circuit Current vs. Light Intensity')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('2_'+str(i)+'.png',dpi = 300)
    #plt.show()
    
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
line1, = ax1.plot(data3[0], data3[1], label='Current', marker='o',color = colorset[9])
ax1.set_xlabel('Voltage (V)')
ax1.set_ylabel('Current (mA)')
ax1.set_title('I-V Characteristics of Single-crystal Silicon')
ax1.legend()
ax1.grid(True)

newline1 = np.array(data3[0])*np.array(data3[1])
newline2 = np.array(data3[0])*np.array(data3[2])

ax11 = ax1.twinx()
line2, = ax11.plot(data3[0], newline1, label='Power', marker='x',color = colorset[0])
lines = [line1, line2]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper right")

line1, = ax2.plot(data3[0], data3[2], label='Current', marker='o',color = colorset[9])
ax2.set_xlabel('Voltage (V)')
ax2.set_title('I-V Characteristics of Amorphous Silicon')
ax2.legend()
ax2.grid(True)

ax22 = ax2.twinx()
line2, = ax22.plot(data3[0], newline2, label='Power', marker='x',color = colorset[0])
ax22.set_ylabel('Power (mW)')
ax2.legend(lines, labels, loc="upper right")

plt.tight_layout()
plt.savefig('3.png',dpi = 300)
#plt.show()

print(newline1)
print(newline2)
