class class1:
    x=1 #like static members in C++
y=class1()
z=class1()
print(y.x)
del z


class placeholder:
    pass


class class2:
    def __init__(self,TeamName, TeamPrincipal, Titles = 8):#forgot to add self, so don't forget that. P.S. 'self' doesn't have to named 'self'. It could be called anything like 'self1'
        self.TeamName = TeamName#instantces of objects
        self.TeamPrincipal = TeamPrincipal
        self.Titles = Titles
    def return_Titles(self): return self.Titles
    def __str__(self): #magic 'dunder' methods that are invokved automatically when objekts are called
        return f"{self.TeamName} head by {self.TeamPrincipal} has {self.return_Titles()} constructor titles"
    def add_WCC(self):
        self.Titles +=1
        print(f"Congratulations! {self.TeamName} has one a constructors Title. {self.TeamName} has now {self.Titles} Titles")

MercedesAMG = class2("Mercedes AMG Petronas", "Mister Toto Wolff")
print(MercedesAMG.TeamPrincipal, MercedesAMG.Titles)
print(MercedesAMG)
MercedesAMG.add_WCC()
del class2.add_WCC #delete from class when deleting methods
del MercedesAMG.Titles
MercedesAMG.T = 8 #adding new property