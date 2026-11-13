import numpy as np
from numpy import random
import scipy; from scipy import stats
import matplotlib.pyplot as plt
x = np.array(random.randint(10, size=10))
y = np.array(random.randint(100, size=10))
slope, intercept, CorrelationCoeff, p, standardError = stats.linregress(x,y)
def find_y(x):
    return slope*x+intercept
print(CorrelationCoeff, find_y(3)) #linear regression prediction is only good when 
regressionModel = list(map(find_y, x)) #list(map(function, iterable))
plt.scatter(x,y)
plt.plot(x, regressionModel)
plt.show()

