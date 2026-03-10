class Bank:
    def __init__(self, name, accType, id, iniDeposit):
        self.name = name
        self.accType = accType
        self.id = id
        self.bal = iniDeposit
    
    def deposit(self, amnt):
        self.bal += amnt
    
    def withdraw(self, amnt):
        self.bal -= amnt
    
    def displayAmnt(self):
        # self.deposit(200)
        # self.withdraw(100)
        print(self.bal)


b1=Bank("Aditi", "Savings", 101, 20000)
b2=Bank("Ram", "Current", 103, 20000)
b3=Bank("Radha", "Savings", 108, 30000)
b1.deposit(5623)
b1.withdraw(623)
b1.displayAmnt()
b2.deposit(8956)
b2.withdraw(800)
b2.displayAmnt()
b3.deposit(12365)
b3.withdraw(200)
b3.displayAmnt()