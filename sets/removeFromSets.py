set1={"MJ", "Freddie", "Sinatra", "Lenon"}
set1.remove("Lenon")
#set1.remove("Jordan") will raise an error since "Jordan" doesn't exist in the set already, so use discard()
set1.discard("Jordan"); set1.discard("Sinatra")
print(set1)

#pop() will remove a random item
x = set1.pop()
print(x)
print(set1)

set1.clear()
print(set1)

del set1