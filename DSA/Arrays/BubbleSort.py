#what I did
arr = [7,12,9,11,3]
print(arr)
i=0
while i<(len(arr)-1):
    j = 0
    while j<(len(arr)-1):
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            #From W3, you could just do arr[j],arr[j+1] = arr[j+1],arr[j] in python. Not me implementing the long C method lol
        j+=1
    i+=1
print(arr); print()

#What I learnt from W3
arr = [7,12,9,11,3]
print(arr)
length = len(arr)

for i in range(length-1):
    swappedStatus = False
    for j in range(length-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swappedStatus = True
    if not swappedStatus: #early exit to save reso urces
        break   
print(arr)