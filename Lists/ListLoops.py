dbz = ["Jiren", "Goku", "Vegeta", "Beerus"]
for x in dbz:
    print(x)

i=0; print("\n")
for i in range(len(dbz)):
    print(dbz[i])

i=0; print("\n")
while i<len(dbz):
    print(dbz[i])
    i+=1

print("\n")
[print(x) for x in dbz] #loop using list comprehension