set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
tuple1 = ("Delta", "Limo", "Hotel")

set3 = set1.union(set2)
print(set3); set3.clear()
set3 = set1 | set2
print(set3); set3.clear()

set3 = set1.union(tuple1)
print(set3)

set3 = set3.union(set1, set2)
print(set3)
