import pandas as pd
dataframe_  = pd.read_csv(r"C:\Users\Anwesh\Desktop\Py\Pandas\PandasCleaningData\dataSet2.csv")
dataframe_RemovedNAN = dataframe_.dropna() #terminates rows with null values
#print(dataframe_.to_string(),"\n")
print(dataframe_RemovedNAN.to_string(),"\n\n")

#Pandas4Warning: The inplace keyword in DataFrame.dropna is deprecated and will be removed in a future version (PDEP-8). 💔
dataframe_.dropna(inplace=True) #terminates row with null values in the ORIGINAL DataSet
print(dataframe_.to_string(),"\n\n")

#FillForNAvalues
dataframe_2 = pd.read_csv(r'C:\Users\Anwesh\Desktop\Py\Pandas\PandasCleaningData\dataSet2.csv')
meanCalories = dataframe_2['Calories'].mean()
dataframe_2.fillna({'Calories' : meanCalories}, inplace=True)#note---> :, not =
#dataframe_2.fillna(333, inplace=True) -->This thing doesn't work in Pandas 3.0+, and I am using Pandas4
print(f"Mean Calories = {meanCalories}, replaced NAcalories with mean \n{dataframe_2}")

print(f"modeOfCalorie = {dataframe_2['Calories'].mode()[0]}")
print(f"medianOfCalorie = {dataframe_2['Calories'].median()}")

