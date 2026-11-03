x = lambda a: a+1
print(x(5))

def myFunction(n):
    return lambda a: a+n
add_5 = myFunction(5)
print(add_5(5))

#map syntax -> map(function, iterable)
multiplier = list(map(lambda a,b:a*b, [1,2,3],[4,5,6])) 
#note that if we don't use list() constructor it was return a lazy value like <map object at 0x000001E38D454700>
print(multiplier); 

#filter()
oddOneOut = list(filter(lambda x: x%2==0, [1,2,3,4,5,6,7,8]))
print(oddOneOut)

#sorted()
list1=list(("12","Senna","McLaren"))
sortByStringLen = list(sorted(list1, key = ( lambda x: len(x) ) ))
print(sortByStringLen)


