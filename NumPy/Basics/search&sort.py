import numpy as np
#Search and Sort Array: 
print("Search and Sort Array: ")
arr = np.array([33,44,12,4,81,63])
print(f"Original arr = {arr}")
print(np.where(arr == 6)) # returns array
print(f"Index value of 12 which would satisfy the said order [in a sorted list] = {np.searchsorted(arr, 12, side = "right")}")#default is side = "left"
print(f"Sorted Array = {np.sort(arr)}\n")

arr2 = np.array([[111,2,33],[24,325,26]])
print(f"Original arr = {arr2}")
print(f"Sorted Array = {np.sort(arr2)}\n")

#Filter Array
print("Filter Array:")
filter_arr = [False, True, False, True, False, True] #dimensiona and size of filter array must match
print(arr[filter_arr])
filter_arr = [] #need to make array empty first, else dimension error occurs
for x in arr:
    if x%2==0:
        filter_arr.append(True)
    else: 
        filter_arr.append(False)
print(f"Filter Array Obtained = {filter_arr}") 
print(arr[filter_arr])
filter_arr2 = arr<30
print(arr[filter_arr2])

