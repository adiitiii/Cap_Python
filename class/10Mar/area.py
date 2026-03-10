class Circle:
    radius=eval(input("enter radius:"))
    def area(self):
        return 3.14*(self.radius)**2

    def peri(self):
        return 2*3.14*self.radius
    

c1 = Circle
print(c1.area())
print(c1.peri())