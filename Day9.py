#while loop
#write a progrom to print no. from 1 to 5 using while loop
i=1
while(i<=5):
    print(i)
    i+=1
    
#50-80
i=50
while(i<=60):
    print(i)
    i+=1
    
# even odd
num=int(input("Enter Number"))
while(num>0):
    print(num)
    if(num%2==0):
        print("num is even")
    else:
        print("num is not even")
    break
    
i=1
while True:
    print(i)
    i+=1
    if(i>10):
        break
print("bye")
    
# write a program to accept a number and print factorial
while True:
    num=int(input("Enter Number"))
    fact=1
    while num>0:
        fact=fact*num
        num-=1
    print(f"fact:{fact}")
    ans=input("do you want to continue, press yes or no").lower()
    if ans=="no":
        break
print("bye")


#password program
password=input("Enter Password")#ABc@1233
isdigit=False
isspecial=False
special="!@#%"
if len(password)>=8:
    for p in password:
        if p.isdigit():
            isdigit=True
        elif p in special:
            isspecial=True
    if isdigit==True and isspecial==True:
        print("password is valid")
    else:
        print("invalid password")
else:
    print("password should be atleast 8 character")

# 
    