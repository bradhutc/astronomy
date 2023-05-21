import numpy as np
import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle

data = np.loadtxt('/Users/bradhutc/Downloads/TESS_LC.dat')

mjd=[]
flux=[]
err=[]

for i in range(len(data)):
    mjd.append(float(data[i][0])-2450000)
    flux.append(float(data[i][1]))
    err.append(float(data[i][2]))


fig = plt.figure(figsize=(10,15))
plt.xlim(8960,8962)
plt.scatter(mjd,flux)
plt.xlabel("Time (MJD)")
plt.ylabel("Power (W)")
plt.title("Transit Depth")
plt.errorbar(mjd,flux,yerr=err,fmt=".k")
plt.show()

frequency, power = LombScargle(mjd, flux).autopower()

#BLS Box Least Squares
    
#Transit Depth
# plt.plot(1/frequency, power)  
# plt.xlabel("Time")
# plt.ylabel("Power")
# plt.title("Transit Depth")
# plt.xlim(8960.50,8961.75)
# plt.ylim(0.98,1.02)
#plt.errorbar(1/frequency,power,yerr=err, fmt=".k")
#plt.show()

#Period vs Power
plt.plot(1/frequency, power)  
plt.xlabel("Frequency")
plt.ylabel("Power")
plt.title("Period vs Power")
plt.xlim(0.0124,0.0125)
plt.show()

print(np.argmax(power))
P=1/frequency
print(1/P[34627])
