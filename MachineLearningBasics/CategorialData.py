import numpy as np
from sklearn import linear_model
import pandas as pd

df = pd.read_csv(r'MachineLearningBasics\DataForCategorialData.csv')

#OneHotEncoding-> So this is basically like Encoders and Decoders in Digital logics
OHEcars = pd.get_dummies(df[['Car']])
#OHEcars = pd.get_dummies(df, columns=['Car'], drop_first=True)
print(OHEcars.to_string())

X = pd.concat([df[['Volume', 'Weight']], OHEcars], axis=1)
y = df['CO2']

regressionObject = linear_model.LinearRegression()
regressionObject.fit(X,y)
input_df = pd.DataFrame([[1600, 1150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]], columns=X.columns)
predictedCO2 = regressionObject.predict(input_df)#audi
print(f"\npredictedCO2 for an Audi with Volume = 1600 and Weight = 1150 is {predictedCO2}\n")


#Dummy Columns
df_ = pd.DataFrame({'colors' : ['Paraguay','Pink', 'Purple']})
df__ = pd.get_dummies(df_, drop_first=True)
#if Pink and Purple both are False, then since this thing is mutually exclusive, the color will be recognized as Paraguay. 
#It eliminates the Multicollinearity redundancy issue. x+y+z = 1 then x = 1-x-y
print(df__.to_string())

