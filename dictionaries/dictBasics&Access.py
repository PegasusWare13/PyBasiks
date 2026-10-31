SccuderriaFerrari = {
    "TP " : "Fred",
    "Driver_1" : "Hamilton",
    "Driver_2 " : "Leclerc",
    "Nickname" : "Hopium Exploiters",
    "LastTitle" : 2007
}
print(SccuderriaFerrari)
print(SccuderriaFerrari["Nickname"])
print(type(SccuderriaFerrari))
print(len(SccuderriaFerrari))

#.get()
x = SccuderriaFerrari.get("LastTitle"); print("\n")

#keys
List_of_keys = SccuderriaFerrari.keys()
print(List_of_keys)
SccuderriaFerrari["BestDriver"] = "Schumacher"
print(List_of_keys)
if 'LastTitle'  in SccuderriaFerrari:
    print("'LastTitle' exists in dictionary SccuderriaFerrari", "\n")

#values()
List_of_values = SccuderriaFerrari.values()
print(List_of_values)
SccuderriaFerrari["Nickname"] = "Bottlers"
print(List_of_values, "\n")

#items
List_of_items = SccuderriaFerrari.items()
print(List_of_items)
SccuderriaFerrari["Nickname"] = "Best Strategists"
print(List_of_items, "\n")