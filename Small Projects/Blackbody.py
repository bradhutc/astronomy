import matplotlib.pyplot as plt
import numpy as np

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

def p(lam, T):
    a = 2.0*h*c**2
    b = h*c/(lam*k*T)
    intensity = a/((lam**5) * (np.exp(b) - 1.0))
    return intensity

wav = np.arange(1e-9, 3e-6, 1e-9) 

i4k = p(wav, 4000.)
i5k = p(wav, 5000.)
i6k = p(wav, 6000.)

plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.plot(wav*1e9, i4k, 'r-', label='4000 K') 
plt.legend(loc="upper right")
plt.plot(wav*1e9, i5k, 'g-', label='5000 K')
plt.legend(loc="upper right")
plt.plot(wav*1e9, i6k, 'b-', label='6000 K') 
plt.legend(loc="upper right")
plt.title('Blackbody Curves of Stars')
plt.show()

