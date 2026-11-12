import pandas as pd
print(f"Max Rows: {pd.options.display.max_rows}")
pd.options.display.max_rows = 1000; print("Set Max Rows to 1000\n")

dataframe1 = pd.read_csv(r'C:\Users\Anwesh\Desktop\Py\Pandas\data.csv') #interpreter will treat \ as an escape sequence character so use r a.k.a. 'raw string'
print(dataframe1.to_string(),"\n\n")
#print(dataframe1)

dataframe2 = pd.read_json(r"C:\Users\Anwesh\Desktop\Py\Pandas\data.json")
print(dataframe2.to_string())