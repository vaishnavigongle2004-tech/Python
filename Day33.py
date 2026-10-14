#encapsulation : private atttribute example
class Account:
    def __init__(self,actno,balance):
        self.actno=actno #public attribute
        self.__balance=balance#private attribute
        
a=Account(111,1000)
print(a.actno)
#print(a.balance) error
print(a._Account__balance)#accesing priavte atttribute using name mangling

#private attribute with method
class Account:
    def __init__(self,actno,balance):
        self.actno=actno#public attribute
        self.__balance=balance#private attribute
    #private method
    def __showbalance(self):
        print(f"balance is {self.__balance}")
a=Account(111,1000)
print(a.actno)
#print(a.balance) error
print(a._Account__balance)#accesing attribute using name mangling
a._Account__showbalance()

#encapsulation:private attribute and public method
class Account:
    def __init__(self,actno,balance):
        self.actno=actno#public attribute
        self.__balance=balance#private attribute
    #public method
    def showbalance(self):
        print(f"balance is {self.balance}")
a=Account(111,1000)
print(a.actno)
a.showbalance()

#encapsulation : protected attribute and public method
class Account:
    def __init__(self,actno,balance):
        self.actno=actno #public attribute