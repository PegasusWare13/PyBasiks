import numpy as np
from numpy import random
import matplotlib.pyplot as pyp
import seaborn as sb

#Binomial Distribution is Discrete
#n = Normal of trials
#p = probability for each trial
sb.displot(random.binomial(size = (100), p = 0.6, n = 3))
pyp.show()

sb.displot(random.binomial(size = (100), p = 0.6, n = 3), kind='kde')
pyp.show()

#So size=9 and size=(3,3) are statistically identical, in that the simulation will occur 9 times in both the cases
sb.displot(random.binomial(size = (2,3), p = 0.6, n = 3))
pyp.show()

sb.displot(random.binomial(size = (3,3), p = 0.6, n = 3), kind='kde')
pyp.show()