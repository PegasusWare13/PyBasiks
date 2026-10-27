list1 = ["Protein", "Carbs", "Fat", "Carbs", "Potassium", "Magnesium", "Calcium"]

newList = []
for x  in list1:
    if "Carbs" in x:
        newList.append(x)
print(x)

newList_2 = []
newList_2 = [x for x in list1 if "M" in x]
print(newList_2)

newList_3 = [x for x in range(5)]
