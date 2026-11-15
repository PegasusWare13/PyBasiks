import numpy as np
from sklearn import linear_model
from numpy import random as r
#Logistic Regression is for discrete data unlike Normal Linear Regression which runs over an equation i.e. continuous data
#data from W3

#x->Features, y->Labels
#skit-learn expects features to be 2D Structures (2D array or Dataframes). 
#We cannot send 1D numpy arrays or pandas series as features. We gotta convert them into 2D Structures. Hence, the reshape for the feature
x_TumorSize = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1) 
y_Cancerous = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])


#DiscretePrediction
RegressionObject = linear_model.LogisticRegression()
RegressionObject.fit(x_TumorSize, y_Cancerous)
inputValue = r.choice(r.uniform(1,6,1))
prediction = RegressionObject.predict(np.array([inputValue]).reshape(-1,1))
print(f"Is the Tumor Size {inputValue}mm Cancerous? {prediction[0]}\n")


#SLOPEofLogarithmicOdds
slope_of_logarithmicOdds = RegressionObject.coef_ #.coef_ returns slope m, not the actual log_odds as told in the w3 website
print("Slope/Coefficient of Logarithmic Odds: ",np.exp(slope_of_logarithmicOdds))
#Since this is basically the slope m = y/x. It tells how much y changes by a unit change in x 
# i.e. how much the outcome/label changes based on a unit change in the feature.
# i.e. how much tumor being cancerous increases by m, with a increase in size of the tumor by 1 unit


#CalculatingProbability
def probability_(regrObject, x_feature):
    logarithmic_odd = regrObject.coef_ * x_feature + regrObject.intercept_
    odds = np.exp(logarithmic_odd)
    #probability = favorableOutcomes/totalOutcomes
    #odds = favorableOutcomes/unfavorableOutcomes
    probability = odds/(1+odds)
    return probability

for x in x_TumorSize:
    prob = probability_(RegressionObject, x)
    print(f"Probability that Tumor of size {x}mm is Cancerous = {prob.item()*100}%")
else: print('\n')
print("Probability of Prediction being correct:",probability_(RegressionObject,x_TumorSize)*100,"%")
