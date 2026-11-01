def display_salary(salary = 1000, experience = 10): #salary and experience are parameters
    print("Salary:",salary," Experience:",experience,"years\n")
display_salary(2000) #default arguments
display_salary(experience=5, salary=500) #order doesn't matter if you specify key=value i.e. non-positional arguments

def ret_List():
    return ["Kakarot", "Whis", "Vegeta"]
dbz = ret_List()
print(dbz, "\n")

def eligiblity(age, /): # we use / to only allow positional arguments and restrict use of keys
    print("Eligible to vote, age =", age,"\n") if age>18 else print("Ineligible to vote age =", age,"\n")
age = 19
eligiblity(age)