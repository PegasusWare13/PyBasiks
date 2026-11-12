#'wrong' is subjective here.
import pandas as pd
dataset_ = pd.read_csv(r'C:\Users\Anwesh\Desktop\Py\Pandas\PandasCleaningData\dataSet2.csv')

for x in dataset_.index:
    if dataset_.loc[x, 'Duration']>180: #syntax-->>.loc[#row, #column]
        dataset_.drop(x, inplace=True)
        #or dataset_.loc[x, 'Duration] = 120

print(dataset_.to_string())