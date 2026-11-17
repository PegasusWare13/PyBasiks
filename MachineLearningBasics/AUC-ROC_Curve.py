import numpy as np
from numpy import random
n=20000
y=np.array([0]*n+[1]*n)
#Okay I get the essence of ROC and AUC scores. 
# It's how well the model can separate between two classes. 
# This keeps in check the tendency of the model to not just be accurate on a single class but entirely fail in another set.
# Hence, I will no longer dwell on this since it doesn't seem an immediate necessity.
# Maybe in the near future.