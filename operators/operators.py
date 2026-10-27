#floor divisor? New stuff for me tbf
print("floor division 12//5 =",12//5, "\n")
#nothing special here tbh. Walrus operators are cool. 
#Apparently they are called so because they resemble the teeth of walruses :=

#WITH WALRUSES
list1 = ["Mercedes", "Ferrari", "McLaren", "Red Bull"]
if(num := len(list1))>0:
    print("list1 isn't empty")
    print("And the list has", num, "elements")
#so with walrus operators, we can compound multiple statements. 

#WITHOUT WALRUSES
list1 = ["Mercedes", "Ferrari", "McLaren", "Red Bull"]
num = len(list1)
if num>0:
    print("list1 isn't empty")
    print("And the list has", num, "elements","\n")

#Ternary operators aren't like from C++ [?:]:
age = 19
VotingEligibility  = True if age>18 else False
print("Eligible for voting:", VotingEligibility, "\n")

#Identity Operators
Push1 = ["Bench Press", "Incline Dumbell Press", "Shoulder Press"]
Push2 = ["Bench Press", "Incline Dumbell Press", "Shoulder Press"]
print("Identity Operators")
print(Push1 is Push2) #checks if Push1 and Push2 have the same memory address
print(Push1 == Push2, "\n") #checks if Push1 and Push2 are equivalent 

#membership operators
WorksTeams = ["Mercedes", "Ferrari", "Red Bull", "AMR Honda", "Audi"]
print("Membership Operators")
print("Mercedes" in WorksTeams)
print("M" not in "Mercedes", "\n")

#Bitwise Operators
#So bitwise operators convert the numbers into binary base
#Then it compares each position bit and return accordingly
# & for and, | for or, ^ for XOR
# (6)10 = (110)2 and (5)10 = (101)2
print("6 & 5 = ", 6&5)
print("6 | 5 = ", 6|5)
print("6 ^ 5 = ", 6^5)
