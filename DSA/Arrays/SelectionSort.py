arr = [64, 34, 25, 5, 22, 11, 90, 12]
length = len(arr)
for i in range(length-1):
    min_index = i
    for j in range(i, length):
            if arr[j]<arr[min_index]:
                  min_index = j
    min = arr.pop(min_index) #pops minindexed value and returns its value to this variable min
    arr.insert(i,min)#inserts min at the relative first index i
    #Or we could swap which is faster since it doesn't have to shift every element of the array when popping
#   arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)

















#THIS ONE WAS THE CLOSEST MATE I FUCKING GIVE UP. I WILL WATCH W3 NOW
# arr = [64, 34, 25, 5, 22, 11, 90, 12]
# length = len(arr)
# for i in range(length-1):
#     j=0
#     min_ = arr[j+i]
#     while j<(length-i-1):
#         if arr[j+i]<min_: 
#             min_ = arr[j+i]
#             indexMin = j+i
#         j+=1
#         shifted = arr
#     for k in range(indexMin):
#         shifted = arr[-1:] + arr[:-1]
# print(arr)
# print(shifted)