'''
types of methods
1. Object Method
called using object

2.class method
can be only accessed using class not object
'''

class Student:
    clg = "JECRC"
    city = 'Jaipur'

    #constructor
    def __init__(self,name,id,age,marks,address): #self keyword is the same as "this" keyword in java
        self.name=name
        self.id=id
        self.age=age
        self.marks=marks
        self.address=address

     #CLASS METHOD
    @classmethod
    def cDisp(cls, n): #mandatory argument in class method is "cls" like self keyword in object method
        cls.clg = n
        print(cls.city)
        print(cls.clg)
    
    def display(self): #object method
        # print(self.name)
        # print(self.age)
        # print(self.id)
        # print(self.marks)
        # print(self.address)
        print(self.clg) 

    #static method
    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def sub(x,y):
        return x-y

#object creation for class
# s1=Student("aditi", 220, 22, 45, "Vaishali") 
# s2=Student("pooja", 2780, 28, 78, "Mansarovar")
# s1.cDisp("pu")
# s1.display()
# s2.display()
# print(Student.sub(10,20))

class Car:
    def __init__(self):
        self.acc=False
        self.clutch=True
        self.brake=False

    def start(self):
        self.acc=True
        self.clutch=True
        print("Car Started...")

c1=Car()
c1.start()
