import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from numpy import random as r

# x = r.uniform(1,15,10)
# y = r.uniform(15,30,10)

#Data from W3
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12] 
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
data = list(zip(x,y))

#Inertia is a measure of how tightly packed the data cluster is.
inertia_arr = []
for i in range(1,11):
    kmeansObject = KMeans(n_clusters=i)
    kmeansObject.fit(data)
    inertia_arr.append(kmeansObject.inertia_)

plt.scatter(x,y)
plt.show()
plt.plot(range(1,11), inertia_arr, marker='o')
#There will be sharp dropoff between in intertia between cluster 1 and 2. So we can say that it will form 2 distinct groups so we pick n_cluster = 2
plt.show()

kmeansObject = KMeans(n_clusters=2)
kmeansObject.fit(data)
plt.scatter(x,y, c=kmeansObject.labels_) #'color' kwarg must be a color or sequence of color specs.  For a sequence of values to be color-mapped, use the 'c' argument instead.
plt.show()