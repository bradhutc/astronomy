import math as m
import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')

#Problem 1.3
a=[0,0.3871,0.7233,1,1.5273,5.2028,9.5388,19.1914,30.0611]
L=[1.04E42,9.1E38,1.8E40,2.7E40,3.5E39,1.9E43,7.8E42,1.7E42,2.5E42]

plt.scatter(a,L,marker='o',color='black')
plt.xlabel('Semi-Major Axis (AU)')
plt.ylabel('Angular Momentum (kg m**2 s**-1)')
plt.xlim(-2,32)
plt.text(5.3,1.8E43,'Jupiter', horizontalalignment='center')
plt.show()

#Problem 1.5
print(sum(L))
print(L[0]/sum(L)*100)

print(L[5]/sum(L)*100)
