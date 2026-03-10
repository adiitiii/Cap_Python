class Emp:
    def __init__(self, name, sal):
        self.Name = name
        self.Salary = sal

class Manager(Emp):
    def __init__(self, name, sal):
        super().__init__(name, sal)
        self.dept = "IT"

    def printDetails(self):
        print(self.Name, self.Salary, self.dept)

m1 = Manager("Aditi", 895656)
m1.printDetails()