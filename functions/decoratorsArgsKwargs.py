def mySwapper(function1):
    def inner(*args,**kwargs):
        for x in args:
            return function1(*args).swapcase()
        for key, x in kwargs:
            return function1(**kwargs).swapcase()
    return inner
@mySwapper
def myFunction(*args,**kwargs):
    # for x in args:
    #     return x
    # for key, x in kwargs.items():
    #     return x, key
    return kwargs, args
print(myFunction("Chuck", "Leclerc", nickname = "LeCrash", number = 16, HomeRace = "Monaco"))


