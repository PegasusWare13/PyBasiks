import pandas as pd
import matplotlib.pyplot as plt
dataframe_ = pd.read_csv(r'C:\Users\Anwesh\Desktop\Py\Pandas\data.csv')
print(dataframe_.corr())
dataframe_.plot()
dataframe_.plot(kind='scatter', x='Duration', y='Calories')
plt.show()
dataframe_['Calories'].plot(kind='hist')
plt.show()
