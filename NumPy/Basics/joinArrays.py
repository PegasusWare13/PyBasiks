import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print("Concatenate=", np.concatenate((arr1,arr2)),"\n")
print("Stack (axis=1) =\n", np.stack((arr1,arr2), axis=1),"\n\n")
print("h-Stack=\n", np.hstack((arr1,arr2)),"\n\n")
print("v-Stack=\n", np.vstack((arr1,arr2)),"\n\n")
print("d-Stack=\n", np.dstack((arr1,arr2)),"\n\n")

arr3 = np.array([[1,2],[3,4]])
arr4 = np.array([[5,6],[7,8]])
print("Concatenate (axis=1) =\n",np.concatenate((arr3, arr4), axis=1))