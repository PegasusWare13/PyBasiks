import numpy as np
from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sb

#I don't even know what this shit is bro. Just doing for the shake of it
#From W3Schools, "Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word."
dis = random.zipf(a=5,size=(1000))
sb.displot(dis[dis<10])
plt.show()