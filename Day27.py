#example of instance attribute
class Customer:
    def __init__(self):
        name=""
        mobile=0
        
c1=Customer()
c1.name="manish"
c1.mobile=123

print(c1.name)
print(c1.mobile)


#example of instance attributes manually
class Customer:
    shopcode=111#class attribute
    
c1=Customer()
c1.name="manish"
c1.mobile=123
print(c1.shopcode)
print(c1.name)
print(c1.mobile)


#example ofconstructor with parameters
class Customer:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
    #method
    def display(self):
       print(f"name : {c1.name}")
       print(f"mobile : {c1.mobile}") 
        
name=input("Enter name")
mobile=int(input("Enter mobile number"))
c1=Customer(name,mobile)
c1.display()

class Phone:
    #class attribute (shared by all instances)
    device_type="Smartphone"
    def __init__(self,brand,model):
        self.device
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("--------Phone details--------")
        print(f"device type {self.device_type}")
        print(f"brand type {self.brand}")
        print(f"price
        
