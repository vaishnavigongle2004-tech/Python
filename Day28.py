#create a class saving
class Saving:
    def __init__(self,actno,bal):
        self.actno=actno
        self.bal=bal
    def deposit(self,amount):
        self.bal=self.bal+amount
        print("amount deposited successfully")
    def show_balance(self):
        return f"balance is {self.bal}"
a=int(input("Enter account number"))
b=int(input("Enter balance"))
s=Saving(a,b)
amt=int(input("enter amount to be deposited"))
s.deposit(amt)
print(s.show_balance())

#example of single inheritance:- child/derived class
#single inheritance interent from one chid class
#example of attribute inheritance
class Person:
    name="vaishnavi"
    address="nagpur"
class Employee(Person):
    empid=123
    salary=50000
e1=Employee()
print(e1.name)
print(e1.address)
print(e1.empid)
print(e1.salary)


#method inheritance
class person:
    def getpersondata(self,name,address):
        self.name=name
        self.address=address
    def displaypersondata(self):
        print(self.name)
        print
    