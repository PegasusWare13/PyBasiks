import numpy as np
from numpy import random
import matplotlib.pyplot as plt

x = np.array([2,3,-3,4,-2])
y = np.array([3,2,-4,6,3])
#unlike seaborn, different plots are combined/overlapped during plt.show()
#Scatter Basics and Color Comparison
plt.scatter(x,y,color='#D68923')
plt.scatter(y,x,color='#56E8D9')
plt.show()
arr_colors = np.array(['r','b','pink','green','purple'])
plt.scatter(x,y,c=arr_colors)
plt.show()

#Scatter ColorMaps --> The array of colors is mandatory, and we can pick from a range of cmaps
x = np.array([random.randint(25),random.randint(25),random.randint(25),random.randint(25),random.randint(25)])
y = random.randint(100,size=(5))
arr_colors = np.array([20,40,60,80,100]) #range->0-100
arr_sizes = np.array([100,180,220,340,600])
plt.scatter(x,y,c=arr_colors, cmap='RdBu',s=arr_sizes, alpha = 0.6)
plt.colorbar()
plt.show()