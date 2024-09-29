import numpy as np

data1 = [[[(171,25),(351,20),(190,15),(10,10)],
          [(161,45),(341,40),(199,59),(19,53)],
          [(151,28),(331,23),(210,17),(30,16)]],
         [[(170,51),(350,48),(190,47),(10,44)],
          [(160,35),(340,31),(201,3),(21,0)],
          [(149,35),(329,29),(212,6),(32,3)]],
         [[(170,49),(350,45),(190,51),(10,47)],
          [(160,30),(340,28),(201,8),(21,5)],
          [(149,29),(329,21),(212,12),(32,9)]]]

data2 = [[(149,13),(329,14),(29,27),(209,30)],
         [(205,24),(25,22),(154,2),(333,58)]]

##我知道这个写的很烂，但是懒得修理了，能跑就行

def dm2r(theta):
    # Convert Degrees_Minutes_2to_Radians
    degrees, minutes = theta[0], theta[1]
    if len(theta) == 3:
        seconds = theta[2]
        total_degrees = degrees + minutes / 60.0 + seconds / 3600.0
    else:
        total_degrees = degrees + minutes / 60.0
    return np.deg2rad(total_degrees)

def mindm(theta1, theta2):
    temp = (60*theta1[0]+theta1[1])-(60*theta2[0]+theta2[1])
    temp %= 360*60
    return (temp//60,temp%60)

def psik(data):
    th1,th2,th1_,th2_ = data[0],data[1],data[2],data[3]
    m1 = mindm(th1_,th1)
    m2 = mindm(th2_,th2)
    temp = ((m1[0]+m2[0])*60+(m1[1]+m2[1]))*15
    temp2 = (int(temp//3600),int((temp%3600)//60),int(temp%60))
    return temp2
def psik2(data):
    th1,th2,th1_,th2_ = data[0],data[1],data[2],data[3]
    m1 = mindm(th1,th1_)
    m2 = mindm(th2,th2_)
    temp = ((m1[0]+m2[0])*60+(m1[1]+m2[1]))*30
    temp2 = (int(temp//3600),int((temp%3600)//60),int(temp%60))
    return temp2
tex = ['\\textbf{绿光}','\\textbf{黄光1}','\\textbf{黄光2}']

data23 =[[],[],[]]
print('\nlatex格式计算数据1:')
for i in range(3):
    
    print(tex[i],end='')
    for j in range(3):
        result = psik(data1[i][j])
        data23[i].append(result)
        print(' & $'+str(result[0])+'^\circ '+str(result[1])+'\' '+str(result[2])+'\"'+'$',end='')
    print('\\\\')
    
print('\nlatex格式计算数据2:')

data = [[],[],[]]
for i in range(3):
    
    print(tex[i],end='')
    for j in range(3):
        result = np.sin(dm2r(psik(data1[i][j])))*10000/((j+1)*3)
        data[i].append(result)
        print(' & $'+str(round(result,3))+'$',end='')
    print('\\\\')
    
print('\nlatex格式计算数据3:')
meandata = []
print('$\overline{\lambda}$',end='')
for j in range(3):
    result = (data[j][0]+data[j][1]+data[j][2])/3
    meandata.append(result)
    print(' & $'+str(round(result,3))+'$',end='')
print('\\\\')
stddata = [546.1,577.0,579.1]
print('$\\varepsilon$',end='')
for j in range(3):
    print(' & $'+str(round(100*np.abs(stddata[j]-meandata[j])/stddata[j],3))+'\% $',end='')
print('\\\\')

print('\nlatex格式计算数据4:')
for i in range(3):
    print('$D_'+str(i+1)+'$ &',round(0.3*(i+1)/(np.cos(dm2r(data23[1][i]))),6),'&',round(0.3*(i+1)/(np.cos(dm2r(data23[2][i]))),6),'\\\\')
    
print('\nlatex格式计算数据5:')


resfuk = psik2(data2[0])
tempetmep = 180*3600 - resfuk[0]*3600 - resfuk[1]*60 - resfuk[2]
resdsd1 = (tempetmep//3600,tempetmep%3600//60,tempetmep%60)
print('A = ',resdsd1)

resfukk2 = psik2(data2[1])

print('delta = ',resfukk2,'\n')

n = np.sin((dm2r(resdsd1)+dm2r(resfukk2))/2)/np.sin(dm2r(resdsd1)/2)

print('n = ',n)

