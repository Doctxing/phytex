import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_H(U,R,l,N=150):
    return U*N/(R*l)

def get_B(U,R,C,S,N=150):
    return U*C*R/(S*N)

c2rdata = [[8.5,71,4.9],[5.5,73,6]]

data = [[[532,333,232,139,65.3,-48,-141,-195,-295,-395,-535,-295,-155,-48,25.3,119,172,232,345,419,532],
         [17.2,16.2,15.2,14,12.4,7.6,0,-4.6,-10.4,-13.6,-15.8,-14.8,-13,-10.6,-7.4,-0.4,4.2,8.8,13.4,15.8,17.2]],
        [[0,66.7,127,160,193,227,267,320,360,460,507],
         [0,2.8,5.6,7.6,9.2,10.4,11.6,13.6,14.4,16.4,17.2]],
        [[1490,1010,490,73.3,-110,-243,-360,-477,-593,-743,-910,-1490,-510,-93.3,223,340,540,707,840,1090,1490],
         [40.4,38.8,35.6,31.6,27.6,22,15.6,0.4,-15.6,-25.2,-31.6,-39.6,-35.6,-30.8,-22.8,-14.8,8.4,24.4,30.8,35.6,40.4]],
        [[0,207,273,307,373,557,657,773,1010,1220,1470],
         [0,7.6,12.4,15.6,20.4,27.6,30.8,33.2,36.4,38.8,40.4]]]

colorset = sns.color_palette("RdBu", 10)
for i in range(2):
    plt.figure(figsize=(12, 6))
    if i == 0:
        ll = 0.13
        ss = 1.24e-4
    else:
        ll = 0.075
        ss = 1.2e-4
    
    templine1 = [[get_H(x*1e-3,c2rdata[i][0],ll) for x in data[2*i][0]],[get_B(x*1e-3,c2rdata[i][1]*1e3,c2rdata[i][2]*1e-6,ss) for x in data[2*i][1]]]
    templine2 = [[get_H(x*1e-3,c2rdata[i][0],ll) for x in data[2*i+1][0]],[get_B(x*1e-3,c2rdata[i][1]*1e3,c2rdata[i][2]*1e-6,ss) for x in data[2*i+1][1]]]

    plt.subplot(1, 2, 1)
    plt.plot(templine1[0],templine1[1],color = colorset[9*i])
    plt.xlabel('Magnetic Field (H)')
    plt.ylabel('Magnetization (M)')
    plt.title('Saturation Hysteresis Loop')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(templine2[0],templine2[1],color = colorset[9*i])
    plt.xlabel('Magnetic Field (H)')
    plt.ylabel('Magnetization (M)')
    plt.title('Initial Magnetization Curve')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(str(i)+'.png',dpi=300)
    #plt.show()