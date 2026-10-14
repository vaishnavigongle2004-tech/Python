# positional argument
#function
# create a function display to print("hello from itp")
def display():
    print("hello from itp")
    print("your current batch is dads")
print("calling the function parameters")
display()
print("again calling the function parameters")
display()


# function square with one parameter to square the number
def square(num):
    sq=num*num
    return sq
num=int(input("Enter Number"))
result=square(num)
print(f"square of a number:{result}")


# function to print factorial of a num
def factorial(num):
    fact=1
    while(num>0):
        fact=fact*num
        num-=1
    return fact
n=int(input("Enter Number"))
result=factorial(n)
print(f"factorial:{result}")

# create a function caculate with 3 parameter to accept 2 no and 1 operator
def calculate(n1,n2,op):
    result=0
    if op=='+':
        result=n1+n2
    elif op=='-':
        result=n1-n2
    elif op=='*':
        result=n1*n2
    else:
        print("invalid operator")
    print(f"result:{result}")
num1=int(input("Enter Number 1"))
num2=int(input("Enter Number 2"))
operator=input("Enter operator(+,-,*)")
calculate(num1,num2,operator)

# function to check username or password
def check(username,password):
    if username=="admin" and password=="admin123":
        print("login sucessufull")
    else:
        print("invalid username and password")
u=input("Enter username")
p=input("Enter password")
check(u,p)

# function calculate with 3 argument to accept 3 subject marks and print total and percentage and grade
#function calculate with one argument to accept unit and calculate bill_amount
