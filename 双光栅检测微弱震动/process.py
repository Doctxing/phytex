import numpy as np 

data = [[504.735,504.635,504.535,504.435,504.335,504.235,504.135,504.035,503.935],
        [2.93,3.40,4.64,7.34,16.52,15.12,12.82,11.05,10.34]]

import matplotlib.pyplot as plt

data = np.array(data)
plt.figure(figsize=(10, 6),dpi=300)
plt.plot(data[0], data[1]*5)
plt.title('Curve')
plt.xlabel(r'Frequency ($Hz$)')
plt.ylabel(r'Amplitude ($\mu m$)')
plt.grid()
plt.savefig('curve.png',dpi = 300)
plt.show()