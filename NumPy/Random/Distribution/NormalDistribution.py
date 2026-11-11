import numpy as np
from numpy import random
import matplotlib.pyplot as pyp
import seaborn as sb

print(f"random.normal(size=(2,3)) = {random.normal(size=(2,3))}")
#Normal Distribution is Continuous
#loc means where the peak of the bell exists (in the horizontal axis)
#scale = standard deviation
arr = random.normal(scale = 0.3, loc = 3, size=(2,3))
sb.displot(arr, kind='kde')
pyp.show()