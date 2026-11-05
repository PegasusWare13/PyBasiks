import numpy as np
print(f"1-Dimensional:")
arr = np.array([33,44,12])
print(arr)
print(type(arr),"\n\n"); 


#2-Dimensional Array
print(f"2-Dimensional:")
arr2 = np.array([[1,2,3],[4,5,6]])#3x2x(1) size
print(arr2)
print(f"Dimension of arr2 = {arr2.ndim}, Shape = {arr2.shape}\n\n")


#3-Dimensional 
print(f"3-Dimensional: ")
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])#3x2x2 size
print(arr3)
print(f"Dimension of arr3 = {arr3.ndim}, Shape = {arr3.shape}")# goated website btw: https://arrayviz.com/
print(f"Element [1,1,1] = {arr3[1,1,1]}\n\n")


#Create array with custom dimension
print(f"Create array with custom dimension:")
arr4= np.array([1,2,3,4], ndmin=3) #note it's nd(m)in, not ndim
print(arr4)
print(f"Dimension of arr4 = {arr4.ndim}, Shape = {arr4.shape}\n\n")

#Array Slicing, Note NumPy slicing isn't inclusive unlike Python slicing that I'd learnt earlier
print(f"Array Slicing:")
arr5 = np.array([[1,2,3,4,5,6],[8,9,10,11,12,13]])
print(f"arr[0,0:5:2] = {arr5[0,0:5:2]}")
print(f"arr[0:,0:5:2] = \n{arr5[0:,0:5:2]}\n\n") #0: == 0:2, :2 == 0:2

#numpy datatypes
print(f"NumPy Datatypes")
arr6 = np.array([0.00,1.2,1,323,22.1,0], dtype='f')
newArr6 = arr6.astype('i4') #or arr6.astype(int) #or arr6.astype('i')
print(f"newArr6 = {newArr6} and dtype = {newArr6.dtype}")
newArr6 = arr6.astype('?') #or arr6.astype(bool)
print(f"newArr6 = {newArr6} and dtype = {newArr6.dtype}")
newArr6 = arr6.astype('S') #or arr6.astype(int) #or arr6.astype('i')
print(f"newArr6 = {newArr6} and dtype = {newArr6.dtype}\n\n")


#copyVsView
arr7 = np.array([33,44,12,16,4])
viewArr7 = arr7.view()
copyOfArr7 = arr7.copy()
print(f"arr7 = {arr7}")
arr7[0]= 3
print(f"In arr7, changed arr7[0] from 33 to 3")
print(f"viewArr7 = {viewArr7}, base = {viewArr7.base}") #it's kinda like reference variables in c++
print(f"copyOfArr7 = {copyOfArr7}, base = {copyOfArr7.base}")

#reshape
arr8 = np.array([1,2,3,4,5,6,7,8,9,10])
print(f"arr8 = {arr8}")
newArr8 = arr8.reshape(5,2)
print(f"newArr8 = \n{newArr8}")
newArr8 = arr8.reshape(-1) #flatenning array
print(f"flatenned newArr8 = {newArr8}")
newArr8 = arr8.reshape(5,2,-1)
print(f"newArr8 = \n{newArr8}\n\n\n")

