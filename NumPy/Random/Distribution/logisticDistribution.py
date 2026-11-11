#Difference Between Logistic and Normal Distribution
#Both distributions are near identical
#But logistic distribution has more area under the tails, meaning it represents more possibility of occurrence of an event further away from mean.
#For higher value of scale (standard deviation) the normal and logistic distributions are near identical apart from the peak.
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sb

#Paramaters: loc, scale, size. Same as Normal Distribution
lowStdDev = {
    "NormalDistribution" : random.normal(size=(50)), #scale (standard Deviation) = 0 by default
    "LogisticDistribution" : random.logistic(size=(50))
}#Have to pass use 1D array when passing to seaborn through a dictionary
HighStdDev = {
    "NormalDistribution" : random.normal(scale = 12, size=(50)), #scale (standard Deviation) = 0 by default
    "LogisticDistribution" : random.logistic(scale = 12,size=(50))
}
sb.displot(lowStdDev, kind='kde')
plt.show()
sb.displot(HighStdDev, kind='kde')
plt.show()