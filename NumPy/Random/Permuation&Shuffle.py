import numpy as np
from numpy import random as r

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