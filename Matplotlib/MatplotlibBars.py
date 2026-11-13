import numpy as np
import matplotlib.pyplot as plt
x = np.array(["David Laid", "CBUM", "Sam Sulek"])
y = np.array([177, 197, 204])
plt.xlabel("Name")
plt.ylabel("Bench PR in KGs", fontdict={'color': 'r', 'size':25})
#VERTICAL BARS
plt.bar(x,y, width=0.5,color = "OliveDrab") #Default Width is 0.8. Color palette: https://www.w3schools.com/colors/colors_names.asp
plt.show()
#HORIZONTAL BARS
plt.barh(x,y, height=0.1,color = "MediumOrchid") 
plt.show()
