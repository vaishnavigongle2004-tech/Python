#Dictionary:popitem
patient={"id":111,"name":"ravi","doctorname":"mahesh"}
print(patient)
p1=patient.popitem()#return last key value and remove it from dict.
print("pop item",p1)
print('remaining',patient)

#update
Patient={"id":"111","name":"ravi","doctorname":"mahesh"}
print(patient)
p1={"doctorname":"sanskar","mobile":43655768790}
patient.update(p1)
print(patient)


patient={}
#adding a new key value pair to dictionary
pid=int(input("enter patient id"))
patient["id"]=pid
pn=input("enter patient name")
patient["name"]=pn
#display the patients
print("patient details")
print(patient)
id=input("enter key to update")
val=input("enter value")
patient.update({id:val})
print(patient)

#copy method of dictionary
tempadd={"area":"sadar","city":"nagpur"}
permadd=tempadd.copy()#creates a duplicate copy of dictionary
print(permadd)


stud={}
for i in range(3):
    name=input("enter name")
    math=int(input("enter math"))
    chem=int(input("enter chem"))
    stud[name]={"math":math,"chem":chem}
print(stud)
             
