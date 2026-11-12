import pandas as pd
dataframe_ = pd.read_csv(r"C:\Users\Anwesh\Desktop\Py\Pandas\data.csv")
print(dataframe_.head(3))#default for head() and tail() is 5
print(dataframe_.tail(3),"\n")
print(dataframe_.info())
