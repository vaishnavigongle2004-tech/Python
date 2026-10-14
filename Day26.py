#example of class attributes
class Student:
    company_name="itpnagpur"
    company_mobile=252356378
    
s1=Student()
s2=Student()
print("s1 details")
print(s1.company_name,s1.company_mobile)
print("s2 details")
print(s2.company_name,s2.company_mobile)
print("student details")
print(Student.company_name,Student.company_mobile)


class Student:
    #create a constructor
    def __init__(self):
        print("constructor called")
        
s1=Student()#it will call constructor automically