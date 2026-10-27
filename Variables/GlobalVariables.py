globalVar = "Global"
def userDefFunction():
    globalVar = "Local"
    print(globalVar)
    global localVar
    localVar = "Local var made global using the Global keyword"
print(globalVar)
userDefFunction()   
print(localVar)
print() 
#To change globalVar value, we use global keyword inside the function
globalVar2 = "Global 2"
def userDefFunction2():
    global globalVar2
    globalVar2 = "Modified Global 2"
    print(globalVar2)
print(globalVar2)
userDefFunction2()
