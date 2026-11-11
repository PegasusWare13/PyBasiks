import numpy as np
from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sb

dis = random.zipf(a=5,size=(1000))
sb.displot(dis[dis<10])
plt.show()