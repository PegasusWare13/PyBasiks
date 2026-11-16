import numpy as np
from sklearn import datasets, linear_model
#default value of c=1. Set high value for Reliable Data and vice versa. 
#Use method .setparams()
iris = datasets.load_iris()
X = iris['data']
y = iris['target']

regressionObject = linear_model.LogisticRegression(max_iter=1000)

C = np.linspace(0.25,3,10).tolist()
score_arr = []
for choice in C:
    regressionObject.set_params(C = choice)
    regressionObject.fit(X,y)
    score_arr.append(regressionObject.score(X,y))

for choice, score in zip(C, score_arr):
    print(f"For C = {choice}, score of the Model = {score}")