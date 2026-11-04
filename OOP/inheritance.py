class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self): print(self.name)

class Dog(Animal):
    def __init__(self, name, species, bark):
        super().__init__(name)
        self.species = species
        self.bark = bark
    def bark1(self):
        print(self.bark*2)
d1 = Dog("Rex", "German Shepard", "Woof")
d1.speak()
print(d1.species)
d1.bark1()
