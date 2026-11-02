#okay I finally feeling like I'm seeing some real shit with this one.
def mySwapper(n):
    def mySwapper(function_to_be_passed):
        if n==0:
            def inner(dnf):
                return function_to_be_passed(dnf).swapcase()
            return inner 
        elif n==1: 
            def inner(dnf):
                return function_to_be_passed(dnf).upper()
            return inner
        else:
            def inner(dnf):
                return function_to_be_passed(dnf).lower()
            return inner
    return mySwapper
def overrated(function):
    def inner():
        function() + "is overrated asf"
    return inner
@mySwapper(0)
#@overrated #doesn't work with @overrated yet. Maybe it's cause of mySwapper() taking an argument? Seems so. I will try to fix this later when I know more about decorators and stuff
def Leclerc(dnf):
    return "Red Stroll DNF No. "+ dnf
print(Leclerc('six'))