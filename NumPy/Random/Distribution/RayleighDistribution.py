import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sb

sb.displot(random.rayleigh(size=(1500), scale=0.4),kind='kde')
plt.show()

#At SD = 1 and df = 2, Rayleigh and ChiSquare Distributions are very similar
size_ = random.randint(1000,3000)
ComparisonToChiSquare = {
    "Rayleigh" : random.rayleigh(size=size_,scale=1),
    "ChiSquare" : random.chisquare(size=size_, df=2)
}
sb.displot(ComparisonToChiSquare,kind='kde')
plt.show()