# program to manage student records
names=[] #empty list to store student tuples
while(True):
    print("\n-----Select your choice-------")
    print("1 - Add student Name")
    print("2 - Display all student")
    print("3 - Search student by roll no")
    print("4 - Delete student record")
    print("5 - Exit")

    choice=int(input("Enter choice"))
    
    # 1-ADD STUDENT
    if choice==1:
        r=int(input("Enter roll no"))
        n=input("Enter student Name")
        c=input("Enter course name")
        stud=(r,n,c)
        names.append(stud)
        print("Student Added Succesfully")
        
    # 2-DISPLAY ALL STUDENT
    elif choice==2:
        if not names:
            print("No student record found")
        else:
            print("\nList of Student Details:")
            for i in names:
                print(f"Roll No:{i[0]} | Name:{i[1]} | Course:{i[2]}")
    
    #3-SEARCH STUDENT BY ROLL NO
    elif choice==3:
        search_roll=int(input("Enter roll no to search"))
        found=False
        for i in names:
            if i[0]==search_roll:
                print(f"Found! Roll No:{i[0]} | Name:{i[1]} | Course:{i[2]}")
                found=True
                break
        if not found:
            print("Student not found")
            
    #4-DELETE STUDENT
    elif choice==4:
        delete_roll=int(input("Enter roll no to delete"))
        found=False
        for i in names:
            if i[0]==delete_roll:
                names.remove(i)
                print("Student record deleted succuessfully")
                found=True
                break
        if not found:
            print("student not found")
            
    #5-EXIT
    elif choice==5:
        print("Exiting program.Goodbye!")
        break
    else:
        print("Invalid choice! please enter the choice between 1-5")
        
        

