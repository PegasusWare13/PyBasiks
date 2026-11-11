import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sb

#Multionmial Distribution is an 'improvement?' from Binomial Distribution
#Binomial Distribution has a singular probability whereas Multinomial has pvals for each n

arr = random.multinomial(n = 4, pvals=[0.6,0.1,0.3,0.1],size = 5) #pvals need not sum to 1
print(arr)
sb.displot(arr,kind='kde')
plt.show()