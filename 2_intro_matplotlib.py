"""
Packages 
--------------------------------------------------------------------------
Build in tools to use (and we can add more!)
""" 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,3.14,50)
y = np.cos(x)
plt.plot(x,y,color='red')
plt.show()

"""
Plotting (matplotlib) 
--------------------------------------------------------------------------
Build in tools to use (and we can add more!)
""" 

plt.figure()
plt.plot(x,y)
plt.title('This is the title')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.text(-8,-4,'This is a text')
plt.tight_layout()
plt.show()
plt.savefig('myfilename.png')

"""
Plotting 2
--------------------------------------------------------------------------
Two plots
""" 

theta = np.linspace(0,2*np.pi,100)
x = np.cos(theta)
y = np.sin(theta)

plt.rc('font', size=16)
fig, axs = plt.subplots(1, 2, figsize=(10,2))
axs[0].axis('equal')
axs[0].grid()
axs[1].grid()
axs[0].plot(x,y)
axs[1].plot(2*x,2*y)

# Notice that the axes is different. This can be changed by:
fig, axs = plt.subplots(1, 2, figsize=(10,2), sharey=True)
for a in axs:
    a.axis('equal')
    a.grid()
axs[0].plot(x,y)
axs[1].plot(2*x,2*y)

# Lets add new values and a legend:
axs[1].plot(3*x,3*y)
plt.legend(['First','Second'])

"""
Plotting 3
--------------------------------------------------------------------------
Bar and scatter plots
""" 

N = 5
x = np.arange(N)
y = np.random.rand(N)

fig, axs = plt.subplots(1, 2, figsize=(10,2))
for a in axs:
    a.grid()
axs[0].bar(x,y)
axs[1].scatter(x,y)


for a in axs:
    a.set_xticks(range(5))
    a.set_yticks([0,0.5,1])
    
axs[0].bar(x,y,color=('b','b','b','r','b'),edgecolor='black')
axs[1].scatter(x,y,100,marker='P',color=('b','b','b','r','b'))

