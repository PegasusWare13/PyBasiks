import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([2,-3,5])
y1 = np.array([-5,3,7])
plt.subplot(1,2,1)
plt.plot(x1,y1)
x2 = np.array([-2,3,-5])
y2 = np.array([5,3,-7])
plt.subplot(1,2,2)
#okay, first two arguments of subplot should be the same, to make it look good at least, I guess.
plt.plot(x2,y2)
plt.show()

plt.subplot(2,2,2)
plt.title('Table 2')
plt.plot(x1,y1)
plt.subplot(2,2,1)
plt.title('Table 1')
plt.plot(x2,y2)
plt.subplot(2,2,3)
plt.title('Table 3')
plt.plot(y1,x1)
plt.subplot(2,2,4)
plt.title('Table 4')
plt.plot(y2,x2)

plt.show()