import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sb

#Parameters: df = Degree of Freedom, and size
arr = random.chisquare(df = 6,size=(50,5))
sb.displot(arr)
sb.displot(arr,kind='kde')
plt.show()