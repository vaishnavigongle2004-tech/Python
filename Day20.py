#variable length argument
def cal_fees_amount(*args):
    l=len(args)
    total=0
    for i in range(l):
        total=total+args[i]
    return total
amount1=float(input("Enter amount 1:"))
amount2=float(input("Enter amount 2:"))
amount3=float(input("Enter amount 3:"))
Total=cal_fees_amount(amount1,amount2,amount3)
print(f"total fees amount paid :{Total} Rs.")