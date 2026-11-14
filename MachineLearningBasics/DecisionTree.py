import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

dataframe_ = pd.read_csv(r'MachineLearningBasics\dataDecisionTree.csv')

nationalityDict = {'UK':0, 'USA':1, 'N':2}
GoDict = {'YES':1, 'NO':0}
dataframe_['Nationality'] = dataframe_['Nationality'].map(nationalityDict)
dataframe_['Go'] = dataframe_['Go'].map(GoDict)

features = ['Age','Experience','Rank','Nationality']
base = dataframe_[features]
aim = dataframe_['Go'] #Or we could also create 2d df instead of this 1d series, the result wouldn't really vary mathematically 

decisionTreeObject = DecisionTreeClassifier()
decisionTreeObject.fit(base, aim)
tree.plot_tree(decisionTreeObject, feature_names=features)

#print(decisionTreeObject.predict([[25,30,7,0]]))
#Okay if I do this shit as told by W3, it will show this annoying arse error: UserWarning: X does not have valid feature names, but DecisionTreeClassifier was fitted with feature names warnings.warn(
#I don't want this error so I will convert this 2D list thing into a dataframe

input_df = pd.DataFrame([[35,30,7,2]], columns=features)
decision = decisionTreeObject.predict(input_df)

if decision: print("YES") 
else: print("NO")
plt.show()