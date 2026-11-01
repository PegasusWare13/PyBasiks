def display_arg(*arg):
    print("1st element of tuple:", arg[0])
    print("3rd element of tuple:",arg[2])
display_arg(1,"Lando", "Norris"); print("\n")

def display_kwarg(Number, **kwarg):
    print("Number:", Number)
    print("Name:", kwarg["Name"]) #converts to a dictionary 
    print("World Champion Date:", kwarg["WC_Date"],"\n")
display_kwarg(12, Name = "Kimi", WC_Date = "11/1/2026")

def display_combined(Number, *arg, **kwarg):
    print("Number:",Number)
    print("Name:", arg[0])
    print("Status:",arg[1],"")
    for key, x in kwarg.items():
        print(key +":",x) # use + instead of ',' if you don't want to create spaces between the words

display_combined(44, "Lewis Hamilton", "Goat", PolePositions = 105, RaceWins = 106); print("\n")

def unpacking_dictionaries(TP, Driver_1, Driver_2, Nickname, LastTitle):
    print(TP,Driver_1, Driver_2,Nickname,LastTitle,"\n")
SccuderriaFerrari = {#arguments should be of the same name as the keys
    "TP" : "Fred",
    "Driver_1" : "Hamilton",
    "Driver_2" : "Leclerc",
    "Nickname" : "Hopium Exploiters",
    "LastTitle" : 2007
}
unpacking_dictionaries(**SccuderriaFerrari)

def modulo(x,y):
    print("y % x =",y%x)
list1=[4,2]
modulo(*list1)