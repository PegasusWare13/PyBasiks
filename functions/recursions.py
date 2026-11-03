def factorial(n):
    if n == 0 | 1:
        return 1 
    else:
        return n*factorial(n-1)
print(factorial(5))

list1 = [11,2,21,32,4,12,200,13]
def findMin(listParameter):
    if len(listParameter)==1:
        return listParameter[0]
    else:
        min = findMin(listParameter[1:])
        return listParameter[0] if listParameter[0]<min else min
print(findMin(list1),"\n")

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())
