list1 = ["Kakarot", "Whis", "Beerus"]
list2 = ["Albert", "Victoria", "Elizabeth"]

list3 = list1+list2
print(list3)
list3.clear()

for x in list2:
    list1.append(x)
print(list1)
del list1[3:6]

list1.extend(list2)
print(list1)