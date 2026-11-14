import pandas as pd
from sklearn import linear_model
from numpy import random
dataframe_ = pd.read_csv(r'MachineLearningBasics\data.csv')
regressionObject = linear_model.LinearRegression() #This creates a regression object

#Aim--> To predict CO2 emission from Volume and Weight
y = dataframe_['CO2']
x = dataframe_[['Volume', 'Weight']]
regressionObject.fit(x,y)
print(f"Relation Coefficients Obtained: {regressionObject.coef_}")


#If we pass raw numbers directly to .predict(), it will display the following error. Hence, we instead pass a dataframe. 
#UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names warnings.warn(
#W3 has the following syntax but it's kinda outdated
# randomVolume = random.randint(600,2200)
# randomWeight = random.randint(80,130)
# predictedValueAufCO2 = regressionObject.predict([[randomVolume, randomWeight]])
# print(f"When randomVolume = {randomVolume} and randomWeight = {randomWeight}, predictedValueAufCO2 = {predictedValueAufCO2}")

randomVolume = random.randint(600,2200)
randomWeight = random.randint(80,130)
inputDataFrame = pd.DataFrame([[randomVolume, randomWeight]], columns=['Volume', 'Weight']) 
#I had this confusion on whether we were to use the keyword 'index' or 'columns'. It's column because unlike in Pandas\PandasBasicsScratchpad.py where we used Index because the keys of the dictionary ended up as columns and index was for individual row data names, we should pass column names here through 'columns' because .predict() expects column names
predictedValueAufCO2 = regressionObject.predict(inputDataFrame)
print(f"When randomVolume = {randomVolume} and randomWeight = {randomWeight}, predictedValueAufCO2 = {predictedValueAufCO2}")

