# keyword argument
def calculate(n1,n2,op):
    result=0
    if op=='+':
        result=n1+n2
    elif op=='-':
        result=n1-n2
    elif op=='*':
        result=n1*n2
    elif op=='/':
        result=n1/n2
    return result
num1=int(input("Enter Number1"))
num2=int(input("Enter Number2"))
operator=input("Enter operator(+,-,*,/)")
r=calculate(n1=num1,op=operator,n2=num2)#keyword argument
print(r)


# default parameter
def contact(fullname,phonenumber,city="nagpur"):
    print("-----------Contact Detail--------------")
    print(f"full name:{fullname}")
    print(f"phone number:{phonenumber}")
    print(f"city:{city}")
    
#ACCEPT DETAILS
fn=input("Enter Full name")
ph=input("Enter phone number")
ch=input("do you want to enter city press yes or no")
if ch=="yes":
    city=input("Enter city")
    contact(fn,ph,city)
else:
    contact(fn,ph)
    