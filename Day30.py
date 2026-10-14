#example of simple method overriding
class Account:
    def deposit(self):
        print("deposit method of account class")
class Saving(Account):
    #overriding the base class deposit method
    def deposit(self):
        print("deposit method of saving class")
s=Saving()
s.deposit()

#2 exampleb after adding bal and interest
class Account:
    bal=1000
    def deposit(self,amount):
        print("deposit method of account class")
class Saving(Account):
    #overriding the base class deposit method
    def deposit(self,amount):
        self.interest=500
        self.bal=self.bal+amount+self.interest
        print(f"amount deposited , bal is {self.bal}")
s=Saving()
s.deposit(200)

#3 ex
class Account:
    bal=1000
    def deposit(self):
        print("deposit method of account class")
class Saving(Account):
    #overriding the base class deposit method
    def deposit(self,amount):
        self.interest=500
        self.bal=self.bal+amount+self.interest
        print(f"amount deposited , bal is {self.bal}")
class Current(Account):
    def deposit(self,amount):
        self.bal=self.bal+amount
        print(f"amount deposited without interest , bal is {self.bal}")
s=Saving()
s.deposit(200)
c=Current()
c.deposit(200)

#4 ex
class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        return f"name : {self.name}"
class student(person):
    def __init__(self,name,rno):
        super().__init__(name)
        self.rno=rno
    def display(self):
        print(super().display())
        return f"rno : {self.rno}"
s=student("alisha",303)
print(s.display())
