import pandas as pd
dataset_ = pd.read_csv(r'C:\Users\Anwesh\Desktop\Py\Pandas\PandasCleaningData\dataSet2.csv')
print(dataset_.duplicated())
dataset_.drop_duplicates(subset=['Calories'],inplace=True) # or dataset_.drop_duplicates(inplace=True) which checks if ENTIRE row is duplicate or not
print(dataset_.to_string())