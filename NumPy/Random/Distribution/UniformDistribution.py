
import numpy as np
from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sb

arr = random.uniform(low =3, high=10, size = 10)
print(arr)
sb.displot(arr)
plt.show()
sb.displot(arr,kind='kde')
plt.show()