import matplotlib.pyplot as plt
import seaborn as sb
sb.displot([2,1,3,5,7])
plt.show() # I had initially named the file 'seaborn.py' which caused an error, so one should name it something unique to seaborn.py

sb.displot([2,1,3,5,7], kind='kde')
plt.show() 