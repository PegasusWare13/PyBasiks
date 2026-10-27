list1 = ["goku", "Vegeta", "beerus", "Whis"]
list2 = [23,12,111,1,0,-1,21,45,76]
list1.sort(key=str.lower) 
print(list1) #not using str.lower will sort Upper letter words first which is yk kinda inconvenient conventionally speaking
list2.sort()
print(list2)

list2.reverse()
print(list2)

#didn't quite understand custom list sorting, so, I will check it out later when I get a problem