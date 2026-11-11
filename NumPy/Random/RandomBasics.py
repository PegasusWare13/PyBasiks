import numpy as np
from numpy import random as r
#rand(), randint(), choice(): 
print("rand(), randint(), choice(): ")
print(f"r.rand(3)={r.rand(3)}") #the argument inside rand is always some sorta size, unlike in randint() where you can also specify the range 
print(f"r.rand(3,2)={r.rand(3,2)}\n")
print(f"r.randint(3)={r.randint(3,9)}") #single randomint less than 3
print(f"r.randint(3, size = 5)={r.randint(3, size = 5)}\n") #single randomint less than 3
print(f"r.choice([31,231,22,7,66,56,43]) = {r.choice([31,231,22,7,66,56,43])}") 
print(f"r.choice([31,231,22,7,66,56,43],size = (2,2)) = \n{r.choice([31,231,22,7,66,56,43],size = (2,2))}") 
print(f"r.choice([31,231,22,7,66,56,43], p=[0.1,0.2,0.3,0.1,0.1,0.2,0.0], size = (10)) = {r.choice([31,231,22,7,66,56,43], p=[0.1,0.2,0.3,0.1,0.1,0.2,0.0], size = (10))}\n\n") # p must sum to 1 

