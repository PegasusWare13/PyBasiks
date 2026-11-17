import matplotlib.pyplot as plt
from numpy import random as r
from sklearn.neighbors import KNeighborsClassifier
x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

data = list(zip(x,y))
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data, classes)

#to classify a newer point
new_x = r.randint(1,15)
new_y = r.randint(16,26)
new_point = [(new_x, new_y)]
prediction = knn.predict(new_point)
plt.scatter(x+[new_x], y+[new_y], c = classes+[prediction[0]])
plt.text(new_x -2, new_y-1, s=f"Class of new_point: {prediction[0]}")
plt.show()