# accept dayno and dayname using match statement
dayno=int(input("Enter dayno(1-7)"))
match dayno:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("some other day")
        
# accept monthno and monthname
monthno=int(input("Enter monthno(1-12)"))
match monthno:
    case 1:
        print("january")
    case 2:
        print("february")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("july")
    case 8:
        print("august")
    case 9:
        print("september")
    case 10:
        print("october")
    case 11:
        print("november")
    case 12:
        print("december")
    case _:
        print("default")


# accept character and print vowel or not
ch=(input("Enter character"))
match ch:
    case 'a'|'e'|'i'|'o'|'u':
        print("vowels")
    case _:
        print("not a vowel")
        
        
        
# accept 2 numbers and operator and print result using match
n1=int(input("Enter number 1"))
n2=int(input("Enter number 2"))
op=input("Enter operator")
match op:
    case '+':
        result=n1+n2
    case '-':
        result=n1-n2
    case '*':
        result=n1*n2
    case '/':
        result=n1/n2
    case '%':
        result=n1%n2
    case _:
        print("not a valid operator")
print(f"Result:{result}")


# accept score and print grade
score=int(input("Enter score"))
match score:
    case score if score>=90 and score<=100:
        print("grade A")
    case score if score>=80:
        print("Grade B")
    case score if score>=70:
        print("Grade C")
    case score if score>=0:
        print("grade fail")
    case _:
        print("invalid score")
    