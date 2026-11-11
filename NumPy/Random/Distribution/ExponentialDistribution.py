import numpy as np
from numpy import random
import matplotlib.pyplot as pyp
import seaborn as sb

#Exponential Distribution is like the Anti-Christ th Poisson Distribution
#scale in Exponential Distribution is the inverse of lam in Poisson Distribution
#lam means the number of occurences in a given time period
#scale here means the time taken for the given number of occurences to occur

sb.displot(random.exponential(scale=2,size=10),kind='kde')
pyp.show()
