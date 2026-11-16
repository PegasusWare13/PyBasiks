import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
import matplotlib.pyplot as plt

data = datasets.load_wine()
X = data.data
y = data.target

decisionTreeObject = DecisionTreeClassifier(random_state=22)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=22)
OutOfBagMODEL = BaggingClassifier(n_estimators=30, oob_score=True, random_state=22)

OutOfBagMODEL.fit(X_train, y_train)
for i in range(1,4):
    plt.figure(figsize=(12,8))
    plot_tree(OutOfBagMODEL.estimators_[i])#, feature_names=X.columns)
    plt.show()
#If I use .predict(), it will use the 30 estimators to average out a result. Pretty cool, isn't it?