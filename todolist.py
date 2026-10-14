# program for todo list
Todo=[]
while(True):
    print("\n------select your choice-------")
    print("1 - Add Task")
    print("2 - View Task")
    print("3 - Delete Task")
    print("4 - Exit")
    
    choice=int(input("Enter choice"))
    
    #1-ADD TASK
    if choice==1:
        Task=input("Enter Task")
        Todo.append(Task)
        print("Added Task",Task)
        
    #2-VIEW TASK
    elif choice==2:
        if not Todo:
            print("No Task Yet")
        else:
            print("\nyour Task")
        
    
    