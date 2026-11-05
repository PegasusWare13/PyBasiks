import numpy as np

arr1 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr1:
    for y in x:
        for z in y:
            print(z,end=" ")
else: print()
for x in np.nditer(arr1[:,:,::2]):
    print(x,end=" ")
else: print()
for x in np.ndenumerate(arr1):
    print(x)