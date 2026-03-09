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
    
    def display(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.marks)
        print(self.address)


#object creation for class
s1=Student("aditi", 220, 22, 45, "Vaishali") 
s2=Student("pooja", 2780, 28, 78, "Mansarovar")
s1.display()
s2.display()