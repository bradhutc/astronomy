import numpy as np
import matplotlib.pyplot as plt

dims,step_n,step_set = 2,1000,[-1,0,1]
origin = np.zeros((1,dims))

step_shape = (step_n,dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)
start = path[:1]
stop = path[-1:]
# Plot the path
fig = plt.figure(figsize=(8,8),dpi=200)
ax = fig.add_subplot(111)
ax.scatter(path[:,0], path[:,1],c="blue",alpha=0.25,s=0.05);
ax.plot(path[:,0], path[:,1],c="blue",alpha=0.5,lw=0.25,ls='-');
ax.plot(start[:,0], start[:,1],c="red", marker="+")
ax.plot(stop[:,0], stop[:,1],c="black", marker="o")
plt.title("2D Random Walk")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
ab=plt.figure()
plt.show()

x=[17,3,15,-19,-56,-17,4,21,-50,25]
y=[-5,11,-4,-14,-3,-35,-25,-21,-23,14]
print(sum(x)/10)
print(sum(y)/10)

#Problem 1
E=[10.2,1.89,0.66,0.31]
h=4.136E-15
c=3.0E8
l=[]
for x in E:
    l.append(c*h/x)
print(l)