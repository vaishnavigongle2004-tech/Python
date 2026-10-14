# to declare variable to store rno,name,fees
rno=int(input("enter rollno"))
name=(input("enter name"))
fees=float(input("enter a fees amount"))
is_active=bool(input("enter true or false of is active"))
print("----student detail---")
print("Roll No",rno)
print("Name",name)
print("Fees",fees)
print("Is Active",is_active)
#type function is used to check datatype
print(type(is_active))
print(type(name))