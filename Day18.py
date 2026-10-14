#while loop
#print multiplication table of 5
i=1
num=int(input("Enter Number"))#5
while(i<=10):
    print(num,"*",i,"=",num*i)
    i=i+1
    
    
#print factorial of a no
i=1
fact=1
num=int(input("Enter Number"))
while i<=num:
    fact=fact*i
    i=i+1
print("Factorial",fact)

#print sum of frist 5 natuaral number
i=1
sum=0
while i<=5:
    sum=sum+i
    i=i+1
print("sum of first 5 natural number",sum)


#accept 3 subject marks an print total marks using while loop
i=1
total=0
while i<=3:
    marks=int(input("Enter Marks"))
    total=total+marks
    i=i+1
print("Total marks",total)