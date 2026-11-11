import numpy as np
from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sb

#based on the 80/20 Pareto's Principle i.e. 20% of factors cause 80% of the outcomes
#parameters: size, and a = shape paramater? I don't know what that means exactly

sb.displot(random.pareto(a=5,size=(10000)))
plt.show()