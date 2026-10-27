#lists are mutable, ordered and allow duplicate values
list1 = [1, "Verstappen", "Red Bull"]
print("list1[0] =",list1[0])
list1[0]=33 
print("list1[0] =",list1[0])
print("list =",list1, "\n")
print(type(list1), "\n")

#list constructors
list2=list(("12","Senna","McLaren"))
print("list2 =", list2,"\n")

#tuples are immutable, ordered and allow duplicate items
#sets are unmodifiable (but we can append or delete data), unordered and don't allow duplicate members
#dictionaries are modifiable and ordered.

#negative indexing
print("list1[-3] =",list1[-3], "\n") #negative indexing starts from -1 cause of course 0 is neither positive nor zero. Besides 0 would always refer to the first element.

#modification of list items
list3 = ["Schumacher", "Vettel", "Lauda", "Ascari", "Fangio", "Raikonnen"]
list3[1:4] = ["Vettel", "Leclerc", "Hamilton"]
print(list3)
