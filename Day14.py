def calculate(m):
    print(type(m))
    sum=0
    for i in m:
        sum+=i
    print(f"total marks",sum)
#passing tuple to a function
m1=int(input("Enter marks"))
m2=int(input("Enter marks"))
m3=int(input("Enter marks"))
marks=(m1,m2,m3)
calculate(marks)# passing tuple to function


#variable length argument
def calculate(*args):
    print(type(args))
    sum=0
    for i in args:
        sum+=i
    print(f"total marks",sum)

#example of variable length argument(*args) to pass arbitary no. of argument
m1=int(input("Enter marks"))
m2=int(input("Enter marks"))
m3=int(input("Enter marks"))
calculate(m1,m2,m3)

# function returning tuple
def calculate(r):
    area=3.14*r*r
    circ=2*3.14*r
    ci=(area,circ)
    return ci
radius=int(input("Enter radiud"))
result=calculate(radius)
print(f"area of a circle:{result[0]}")
print(f"circumference of a circle:{result[1]:.2f}")


#there are two bulit in function in tuple are count an index
age=(18,20,18,23,24,55)
l=len(age)
print(f"length:{l}")
for i in range(l):
    print(age[i])
num=int(input("enter age"))
c=age.count(num)
print(f"count of age{num} in tuple:{c}")
ind=age.index(num)
print(f"index of {num} is :{ind}")