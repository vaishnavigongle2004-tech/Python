#create a class book
class Book:
    title=None
    author=None
    price=0
b=Book()
print("Enter Book details")
b.title=input("Enter title")
b.author=input("Enter author")
b.price=int(input("Enter price"))
print("Book Details")
print(f"title : {b.title}")
print(f"author : {b.author}")
print(f"price : {b.price}")


#create a class customer having attribute cust_id,cust_name,cust_email,cust_mobile
class Customer:
    cust_id=None
    cust_name=None
    cust_email=None
    cust_mobile=None
C=Customer()
print("Enter Customer Details")
C.cust_id=int(input("Enter customer id"))
C.cust_name=input("Enter customer name")
C.cust_email=input("Enter customer email")
C.cust_mobile=int(input("Enter customer mobile number"))
print("Customer Details")
print(f"customer id : {C.cust_id}")
print(f"customer name : {C.cust_name}")
print(f"customer email : {C.cust_email}")
print(f"customer mobile : {C.cust_mobile}")


#create a classs patient having attribute pat_id,pat_name,disease,doctorname
class Patient():
    pat_id=None
    pat_name=None
    pat_disease=None
    pat_doctorname=None
P=Patient()
print("Enter Patient Details")
P.pat_id=int(input("Enter patient id"))
P.pat_name=input("Enter Patient name")
P.pat_disease=input("Enter Patient disease")
P.pat_doctorname=input("Enter patient doctor name")
print("-------Patient details---------")
print(f"patient id : {P.pat_id}")
print(f"patient name : {P.pat_name}")
print(f"patient disease : {P.pat_disease}")
print(f"patient doctor name : {P.pat_doctorname}")
