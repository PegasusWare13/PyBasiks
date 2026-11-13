import numpy as np
import matplotlib.pyplot as plt
data = np.array([150, 120, 80, 100, 75])
split = np.array(['Push Day', 'Pull Day', 'Legs', 'Upper', 'Lower'])
arrColors = np.array(['red', 'blue', 'black', 'cyan', 'green'])
arrExplode = np.array([0.1,0,0,0.1,0])
plt.pie(data, labels=split, shadow=True, startangle= 30, colors=arrColors,explode=arrExplode)
plt.legend()
plt.show()