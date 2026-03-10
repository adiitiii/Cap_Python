class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    
    def printName(self):
        print(self.firstName, self.lastName)
    
class Child(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Child("Mike", "Olsen")
y = Person("Aditi", "Maheshwari")
x.printName()
y.printName()