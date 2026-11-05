import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print("Concatenate=", np.concatenate((arr1,arr2)),"\n")
print("Stack (axis=0) =\n", np.stack((arr1,arr2), axis=0),"\n\n")#so axis=0 means rows
print("Stack (axis=1) =\n", np.stack((arr1,arr2), axis=1),"\n\n")#so axis=1 means column
print("h-Stack=\n", np.hstack((arr1,arr2)),"\n\n")
print("v-Stack=\n", np.vstack((arr1,arr2)),"\n\n")
print("d-Stack=\n", np.dstack((arr1,arr2)),"\n\n")
arr3 = np.array([[1,2],[3,4]])
arr4 = np.array([[5,6],[7,8]])
print("Concatenate (axis=1) =\n",np.concatenate((arr3, arr4), axis=1),"\n\n") 


arr2D = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14]])
newArr = np.array_split(arr2D,3)
print(f"Split into 3 array into new list along axis = 0 (default):\n{newArr}")
newArr = np.array_split(arr2D,3,axis=1)
print(f"Split into 3 array into new list along axis = 1):\n{newArr}")