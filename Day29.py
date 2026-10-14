#super keyword ex
# class person:
#     def __init__(self,name):
#         print("person class constructor called")
#         self.name=name
# class Student:
#     def __init__(self,name,rno):
#         super().__init__(name) #super is used to call parent class constructor
#         print("student class constructor called")
#         self.rno=rno
#     def display(self):
#         print(self.name)
#         print(self.rno)
# s = Student("amit",345)
# s.display()

#Create a class Person with attributes name and age, and a method display()
#to print them. Create a class Employee that inherits from Person and adds
#an attribute salary with a method to display all details.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def display(self):
        super().display()
        print(f"Salary:{self.salary}")
        
e1=Employee("vaishnavi",21,100000)
e1.display()

# Create a class Vehicle with a method fuel_type() that prints
# "Uses petrol/diesel". Create a class Car that inherits from Vehicle,
# adds a method num_wheels() that prints "4 wheels", and calls both
# methods from an object of Car.
class Vehicle:
    def fuel