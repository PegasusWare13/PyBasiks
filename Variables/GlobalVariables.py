globalVar = "Global"
localVar = "121212"
def userDefFunction():
    globalVar = "Local"
    print(globalVar)
    global localVar
    localVar = "Local var made global using the Global keyword"
print(globalVar)
userDefFunction()   
print(localVar)
print() 

#nonlocal keyword
print()
def parent():
    x = "parent"
    def child():
        nonlocal x
        x = 'child'
        print(x)
    child()
parent()
