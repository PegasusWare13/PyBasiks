import numpy as np
from numpy import random
arr = random.randint(100, size=(20))
print(f"array obtained: {arr}\n")

#Mean, Median, Mode
print("Median, Median, Mode:")
print(f"Mean: {np.mean(arr)}")
print(f"Median: {np.median(arr)}")
import scipy.stats as s #need scipy.stats for mode, it's not in np
print(f"Mode: {s.mode(arr)}\n")

#Variance and Std Deviation
print("Variance and Standard Deviation:")
print(f"Variance: {np.var(arr)}")
print(f"Standard Deviation: {np.std(arr)}\n")

#Percentile
print("Percentiles:")
randomChoice = random.choice(arr)
print(f"Percentile of randomChoice={randomChoice} is {np.percentile(arr, randomChoice)}\n")

