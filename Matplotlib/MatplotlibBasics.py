import matplotlib.pyplot as plt
import numpy as np
ordinates = np.array([1,2,3])
abscissa = np.array([-1,-2,-3])
plt.plot(ordinates,abscissa); plt.show()
plt.plot(ordinates,abscissa, 'o'); plt.show()  #shows just the points
plt.plot([3,-5,2,-12]); plt.show() # if only 1 list is passed, x-coordinates will be set to the default list [0,1,2,3,4....]. They did x dirty here 💔💔

