import bank #bamk is a user defined module having bal variable and 3 function
amount=int(input("enter amount"))
result=bank.deposit(amount)
print(result)
amount=int(input("enter amount to be withdrawal"))
result=bank.withdrawal(amount)
print(result)
