import numpy as np
from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sb

#poisson Distribution has unlimited outcomes unlike Binomial Distrbution where it's just 0 and 1
#lam = rate or known number of occurences
arr = random.poisson(lam = 3, size = 10)
print(arr)
sb.displot(arr)
plt.show()
sb.displot(arr,kind='kde')
plt.show()