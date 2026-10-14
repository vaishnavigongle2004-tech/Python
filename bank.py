#creating a userdefined module named bank.py having variable bal and 3 functions
def deposit(amount):
    bal=1000
    bal=bal+amount
    return f"balance deposited,bal is {bal}"
def withdrawal(amount):
    bal=1000
    bal=bal-amount
    return f"amount withdrawal, bal is {bal}"
def show_balnace():
    bal=1000
    bal=bal-amount
    return f"current bal is {bal}"
#save this file as bank.py