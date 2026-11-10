import numpy as np
from numpy import random as r
#rand(), randint(), choice(): 
print("rand(), randint(), choice(): ")
print(f"r.rand(3)={r.rand(3)}") #the argument inside rand is always some sorta size, unlike in randint() where you can also specify the range 
print(f"r.rand(3,2)={r.rand(3,2)}\n")
print(f"r.randint(3)={r.randint(3)}") #single randomint less than 3
print(f"r.randint(3, size = 5)={r.randint(3, size = 5)}\n") #single randomint less than 3
print(f"r.choice([31,231,22,7,66,56,43]) = {r.choice([31,231,22,7,66,56,43])}") 
print(f"r.choice([31,231,22,7,66,56,43],size = (2,2)) = \n{r.choice([31,231,22,7,66,56,43],size = (2,2))}") 
print(f"r.choice([31,231,22,7,66,56,43], p=[0.1,0.2,0.3,0.1,0.1,0.2,0.0], size = (10)) = {r.choice([31,231,22,7,66,56,43], p=[0.1,0.2,0.3,0.1,0.1,0.2,0.0], size = (10))}\n\n") # p must sum to 1 

#Permutation
print("Permuation: ")
arr = [12,121,232,345,7,4,223,7,9]
print(f"Original arr = {arr}")
print(f"r.permutation(arr) [return a new arr without making changes to Original arr]= {r.permutation(arr)}")
print(f"Original arr after Permuation = {arr}\n")

#Shuffle
print("Shuffle:\n",r.shuffle(arr)) #returns nothing but shuffles the order in the Original arr itself
r.shuffle(arr)
print(f"Original arr after shuffling = {arr}")
