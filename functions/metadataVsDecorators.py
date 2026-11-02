def mySwapper(function1):
    def inner():
        return function1().swapcase()
    return inner
@mySwapper
def HelloWorld():
    return "HeLLo woRLD"
print(HelloWorld.__name__) #use double underscores

import functools
def mySwapper(function1):
    @functools.wraps(function1)
    def inner():
        return function1().swapcase()
    return inner
@mySwapper
def HelloWorld():
    return "HeLLo woRLD"
print(HelloWorld.__name__) #use double underscores
