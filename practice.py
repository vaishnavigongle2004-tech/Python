#write a program to accept bill amount calculate tax(5% if bill_amount<1000, 10%)
bill_amount=int(input("Enter Amount"))
if bill_amount<1000:
    tax=bill_amount*0.05
elif bill_amount>=1000 and bill_amount<5000:
    tax=bill_amount*0.10
else:
    tax=bill_amount*0.15
print("Tax Amount",tax)
total=tax+bill_amount
print("Total Bill Amount",total)


#write a to print even odd
num=int(input("Enter Number"))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")
    

#write a program to print table of any number
num=int(input("enter Number"))
for num in range(1,11):
    