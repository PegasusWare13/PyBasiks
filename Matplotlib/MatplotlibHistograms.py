import numpy as np
import matplotlib.pyplot as plt
from numpy import random
dataDistribution = random.normal(size = 1000, loc =10, scale = 50)
plt.hist(dataDistribution)
plt.show()