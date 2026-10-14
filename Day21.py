#program to accept names
names=[]#empty list
print("select your choice")
print("1-add student names")
print("2-exit")
while(True):
    choice=int(input("Enter choice"))
    if choice==1:
        n=input("Enter student name")
        names.append(n)
    elif choice==2:
        break
print("List of student added")
print(names)


#write a program to print student rollno,name,course
names=[]#empty list
print("select your choice")
print("1-add student names")
print("2-exit")
while(True):
    choice=int(input("Enter choice"))
    if choice==1:
        r=int(input("Enter student rollno"))
        n=input("Enter student name")
        c=input("Enter course")
        stud=(r,n,c)
        names.append(stud)
    elif choice==2:
        break
print("List of students details")
for i in names:
    print(f"roll no:{i[0]}")
    print(f"name:{i[1]}")
    print(f"course:{i[2]}")
    