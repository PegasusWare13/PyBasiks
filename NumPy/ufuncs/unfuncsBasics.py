import numpy as np

print("ufunc type:")
print(type(np.add))
print(type(np.concatenate),"\n")

print("ufunc arithmetic operations:")
print(np.add([1,2,3,4],[6,7,8,9]),"\n")
#likewise we have subtract, div, mod, multiply, divmod, power, absolute

#usercreated ufunc
print("User Created ufunc:")
def multiply(a,b):
    return a*b
multiply = np.frompyfunc(multiply,2,1) #(function, no. of input, no. of output)
print(multiply([1,2,3],[6,7,8]))
print(multiply((1,2,3),(6,7,8)),"\n")

#ufunc Rounding Decimals
print("ufunc Rounding Decimals")
print(f"Truncate: {np.trunc([0.564543534,-1.2323425])}")
print(f"Round: {np.round(23.23123, 2)}") #rounds to 2 decimal places
print(f"Floor: {np.floor([2.2323253,-3.554534])}")
print(f"Ceil: {np.ceil([2.2323253,-3.554534])}\n")

#logarithms
print("Logarithms:")
print(np.log10(np.arange(1,10)))
print(np.log(np.arange(1,10)))
from math import log
logarithm = np.frompyfunc(log,2,1)
print(logarithm(10,4 ),"\n") 

#summation
print("Summation:")
arr1 = np.array([1,2,3])
arr2= np.array([7,8,9])
print(np.sum([arr1,arr2],axis=1))
print(np.cumsum(arr1),"\n")

#products
print("Products:")
print(np.prod([arr1,arr2]))
print(np.prod([arr1,arr2],axis=1),"\n")
print(np.cumprod(arr1),"\n")

#Discrete Differences
print("Differences:")
print(np.diff([5,10,15,20,25]))
print(np.diff([5,10,15,20,25],n=2),"\n")

#LCM
print("LCM")
print(np.lcm(5,6))
print(np.lcm.reduce(arr2),"\n")

#GCD
print("GCD")
print(np.gcd(5,6))
print(np.gcd.reduce(arr2),"\n")

#Trigonometric
print("Trigonometric:")
print(np.sin(np.pi/2))
arr_angles = np.array([0, np.pi/4, np.pi/2, np.pi, np.pi*1.5, np.pi*2])
print(np.sin(arr_angles))
print(np.rad2deg(arr_angles)) 
print(np.deg2rad(np.rad2deg(arr_angles)))
print(np.hypot(3,4))
print(np.arccos(np.sin(arr_angles)),"\n")

#Hyperbolic-sane as trigonometric, just write the hyperbolic suffix at the end i.e. sin()->sinh()

#Set Operations
print("Set Operations:")
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([4,5,6,7,8])
print(np.union1d(arr1,arr2))
print(np.intersect1d(arr1,arr2))
print(np.setxor1d(arr1,arr2))
print(np.setdiff1d(arr1,arr2))
print(np.unique([1,2,3,4,5,5,4,3,7,8])) #can only be 1D




