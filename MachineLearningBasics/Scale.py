import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
import numpy as np
from numpy import random

scale = StandardScaler() #This is important because I previously tried transform() for single numerical dataset but it displayed an error because StandardScaler() hadn't learnt the standard deviations of the entire dataset. 
#But when I use the same object(?) 'scale' for fit_transform() and then transform() subsequently, it will work because it would've already learnt the transform parameters before

dataframe_ = pd.read_csv(r'C:\Users\Anwesh\Desktop\Py\MachineLearningBasics\dataVolumeScaledToLitres.csv')
regression_Object = linear_model.LinearRegression()

#x_df = pd.DataFrame([['2', '90']], columns=['Volume', 'Weight']) #So I figured this won't work subjectively (syntactically it does) because I am only passing a single value for each of Volume and weight but to scale, we need figures such as Standard Deviation and mean. 
#ScaledValue = (GivenValues-Mean)/StandardDeviation
y_series = dataframe_['CO2'] #1-D Series
x_df = dataframe_[['Volume', 'Weight']] #2-D Dataframe
ScaledX = scale.fit_transform(x_df) #scales Weight and Volume relative to each other
print("Scaled Values:\n",ScaledX,"\n")

regression_Object.fit(ScaledX, y_series)
print(f"Regression Coefficients: {regression_Object.coef_}")

#FRANKENSTEIN MONSTER OF A CODE
randomVolume = random.uniform(low=0.6, high=2.2, size=1)
randomWeight = random.randint(80,130)
scaledRandoms = scale.transform([[randomVolume[0], randomWeight]])
input_df = pd.DataFrame(scaledRandoms, columns=['Volume', 'Weight']) 
predictedCO2 = regression_Object.predict(input_df)
print(f"When randomVolume = {randomVolume} and randomWeight = {randomWeight}, predictedCO2 = {predictedCO2}")
