def myFunction():
    yield 5
    yield 6
    yield 7
for x in myFunction(): print(x)
print()

def counter(n):
    i=0
    while i<=n:
        yield i
        i = i+1
for x in counter(10):
    print(x)
