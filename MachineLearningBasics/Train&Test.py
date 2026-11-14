import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#using polynomial regression for this case
x = random.normal(loc = 15, scale = 5, size = 100)
y = random.normal(loc = 500, scale = 30, size = 100) / x

train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

model = np.poly1d(np.polyfit(train_x,train_y,3))

r2_score_ = r2_score(test_y, model(test_x))
print("r2_score =",r2_score_)
points_x = np.linspace(start=1,stop=30,num=100)
plt.scatter(train_x,train_y)
plt.plot(points_x, model(points_x))
plt.show()