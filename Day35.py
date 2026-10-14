'''
#Lambda Function
add=lambda x,y : x+y
print(add(2,3))
sub=lambda a,b : a-b
print(sub(3,1))
mul=lambda x,y:x*y
n1=int(input("enter number 1"))
n2=int(input("enter number 2"))
result=mul(n1,n2)
print(f"multiplication :{result}")
div=lambda x,y:x/y
n1=int(input("enter number 1"))
n2=int(input("enter number 2"))
result=div(n1,n2)
print(f"division :{result}")


#square of a number
sq=lambda x:x**2
n1=int(input("enter number 1"))
result=sq(n1)
print(f"square of a number :{result}")
cb=lambda x:x**3
n1=int(input("enter number 1"))
result=cb(n1)
print(f"cube of a number :{result}")


#concatinate 2 strings
fullname=lambda fn,ln:fn +" "+ln
print(fullname("amit","kumar"))

#even or odd using lambda function
result=lambda x:x%2==0
print(result(6))

#conditional expression:lambda function return largest of two number
result=lambda x,y:x if x>y else y
print(f"greater is :{result(345,41)}")

#string length:lambda function to return the length of string
l=lambda s : len(s)
print(f"length",l("vaishnavigongle"))

#multiply three number
#positive or negative
result=lambda n:"positive" if n>0 else "negative"
print(result(-12))

#map function
res=lambda n:n*n
num=[1,2,3]
result=list(map(res,num))
print(result)

#lambda function to add corresponding elements from two list
number1=[1,2,3]
number2=[4,5,6]
result=list(map(lambda x,y:x+y,number1,number2))
print(result)

#filter function
#the filter() is used to filter elements from an iterable list
#filter even no from iterable
num=[1,2,3,4,5,6,7,8]
result=list(filter(lambda x:x%2==0,num))
print(result)

#sorted function-it used to sort an iterable and return a new sorted list
num=[11,2,33,45,87,32,35]
print(f"before sorting :{num}")
num.sort()
print(f"after sorting :{num}")

#or
numbers=[5,2,8,1,9]
sorted_numbers=sorted(numbers)
print(f"numbers :{numbers}")
print(f"after sorting:{sorted_numbers}")

#reverse list
numbers=[5,2,8,1,9]
sorted_numbers=sorted(numbers,reverse=True)
print(f"numbers :{numbers}")
print(f"after sorting:{sorted_numbers}")
'''

#sort the list with length of fruits using key in sorted method
words=["banana","apple","pineapple","chery","kiwi"]
sorted_words=sorted(words, key=lambda x:len(x),reverse=True)
print(sorted_words)

#sort a list of dictionatries by a specific key:
people=[{"name":"Alice","age":25},{"name":"Bob","age":30},{"name":"Charlie","age":20}]
sorted_people=sorted(people,key=lambda x:x["age"])
print(sorted_people)

