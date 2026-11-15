import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering

x = random.uniform(low=1, high=15, size = 12)
y = random.uniform(low=15, high=30, size=12)
plt.scatter(x,y)
plt.show()

#Unsupervised Learning
data = list(zip(x,y)) #zip converts multiple types of iterable into a uniform lazy zip object. And we use list contructor to convert that zip object into a list
linkageData = linkage(data, method='ward', metric='euclidean')
dendrogram(linkageData)
plt.show()

hierarchial_cluster = AgglomerativeClustering(n_clusters=2, linkage='ward')
labels = hierarchial_cluster.fit_predict(data) 
print(labels)
plt.scatter(x,y,c=labels)
plt.show()

