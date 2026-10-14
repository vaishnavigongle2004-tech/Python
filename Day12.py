#tuple
num=(1,2.2,"hello",True)#explicity type written in braket
print(type(num))
print(num[0])
for i in num:
    print(i)
num1=(11,)#after any no or value you should write a comma so, it consider as tuple
print(type(num1))


#implicit type writtten in without bracket
num=1,2.2,"hello"
print(type(num))
for i in num:
    print(i)
    
num=1,2.2,"hello"
print(type(num))


#slicing in tuple
num=(1,2,3,4,5)
print(num)
print(num[1:4])
print(num[:3])
print(num[3:])
print(num[:2])
print(num[::2])

print(num[::-1])