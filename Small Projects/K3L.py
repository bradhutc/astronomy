import matplotlib.pyplot as plt
import numpy as np

D=np.linspace(0,32)
T=(np.linspace(0,32))**(3/2)

Names=["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
AU=[0.4,0.7,1,1.5,5.2,9.5,19.8,30]
Y=[0.241,0.616,1,1.88,11.86,29.46,84.01,164.79]


#plt.legend(Names)
plt.title("Theoretical Keplerian Curve & Planet Overplots")
plt.xlabel("Semi-Major Axis (AU)")
plt.ylabel("Period (Years)")
plt.plot(D,T)
plt.scatter(AU,Y)

z=0
for i,j in zip(AU,Y):
    plt.text(i,j,Names[z],fontname="Times New Roman", size=13,fontweight="bold")
    z+=1

plt.show()
