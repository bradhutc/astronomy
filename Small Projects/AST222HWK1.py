import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt("/Users/bradleyhutchinson/Desktop/lc.fits.txt")

x=data[:,0]
y=data[:,1]
dy=data[:,2]

from astropy.timeseries import LombScargle
frequency, power = LombScargle(x, y,dy).autopower()

plt.plot(1/frequency, power)  
plt.xlabel("Period")
plt.ylabel("Power")
plt.xlim(0,40)
plt.show()

print(np.argmax(power))
P=1/frequency
print(P[244])

