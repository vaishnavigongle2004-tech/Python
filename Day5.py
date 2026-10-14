# 1. Customer segement classification (retail/e-commerce)
# situaition:
# you are analyzing customer spending data. based on total purchase amount in the last 6 months, classify
# the customer into segments for trageted marketeking.
# 
# rules:
# 
# >=50000-"premium"
# 20000-49999-"gold"
# 5000-19999-"silver"
# <5000-"bronze"

purchase_amount=float(input("Enter total purchase amount:"))
if purchase_amount >= 50000:
    segment="premium"
elif purchase_amount >= 20000 and purchase_amount <= 49999:
    segment="gold"
elif purchase_amount >= 5000 and purchase_amount <= 19999:
    segment="silver"
else:
    segment="bronze"
print(f"Customer segment:{segment}")




target=float(input("Enter montly target:"))
achieved=float(input("Enter actual sales:"))
percentage=(achieved/target)*100
if percentage>=120:
    rating="outstanding"
elif percentage>=100:
    rating="Execellent"
elif percentage>=80:
    rating="Good"
elif percentage>=50:
    rating="Average"
else:
    rating="Needs Improvement"
    
print(f"Achievemnet:{percentage:.2f}%")
print("Performance Rating:",rating)
