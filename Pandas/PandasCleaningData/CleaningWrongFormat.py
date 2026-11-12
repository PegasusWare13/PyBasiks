import pandas as pd
dataframe_ = pd.read_csv(r'C:\Users\Anwesh\Desktop\Py\Pandas\PandasCleaningData\dataSet2.csv')
#NaN --> NaT 
#row-22 has NaN data and row-26 has data in wrong format
dataframe_['Date'] = pd.to_datetime(dataframe_['Date'], format='mixed')
print(dataframe_.to_string(),"\n\n")
dataframe_.dropna(subset=['Date'], inplace=True)
print(dataframe_)