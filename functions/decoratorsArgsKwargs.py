def mySwapper(function1):
    def inner(*args,**kwargs):
        return function1(*args,**kwargs).swapcase()
    return inner
@mySwapper
def myFunction(*args,**kwargs):
    for x in args:
        return x
    for key, x in kwargs.items():
        return x

print(myFunction("Chuck", "Leclerc", nickname = "LeCrash", number = 16, HomeRace = "Monaco"))


# def mySwapper(function1):
#     def inner(*args):
#         return function1(*args).swapcase()
#     return inner
# @mySwapper
# def myFunction(*args):
#     for x in args:
#         print(x)
# myFunction("Chuck", "Leclerc")