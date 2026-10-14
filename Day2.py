# a variable's type can change during execution by assinging a new value of a diffferent type.
num=20
print(type(num))
num=23.44
print(type(num))
num="hello"
print(type(num))

# multiple variable in one line
n1,n2,n3=10,20,30
print(f"num1:{n1},num2:{n2},num3:{n3}")


# type conversion
n1="12"
n2="33.3"
result=float(n1)+float(n2)
print(f"result:{result}")


# converting input ot boolean
'''
Converting Input to Boolean
convert input to a boolean(e.g.,for yes/no questions).
'''
is_student=input("Are you a student? (yes/no):").lower()=="yes"
print("Student status:",is_student) #Output:student status:True
#(if input is"yes")


# accept nultipe inputs
# split input string to accept multiple values.
n1,n2,n3=input("Enter three number(separated by space):").split()
print(f"n1:{n1},n2:{n2},n3:{n3}")
total=int(n1)+int(n2)+int(n3)
print(f"total:{total}")


# program to accept length and breadth in same line and print area
length,bredth=input("Enter a two numbers(separated by space):").split()
print(f"length:{length},bredth:{bredth}")
Area=int(length)*int(bredth)
print(f"Area:{Area}")
# program to accept 5 subject marks in same line and print total and
