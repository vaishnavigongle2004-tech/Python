'''
# proggram to print prime no
# accept a number and print a num is prime or not
num=int(input("Enter Number")) #5
for i in range(2,num):
    if num%i==0:
        print("num is not prime no")
        break
#check if num is not divided by any between no
if num==(i+1):
    print("num is prime no")
'''
'''
# nested fo loop
#program to print prime no. between 1 to 20
for num in range(3,11):
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not prime no.")
         #check if num is not divided by any between no.
    if num==(i+1):
        print(f"{num} is prime no")
'''

principal=1000.0 # $1000 starting ampount
rate=0.05        # 5% annual interest rate
years=4
print(f"Intial Investement {principal}")
#loop through each year from 1 to 4
for year in range(1,year+1):
    