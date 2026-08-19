unit=int(input("enter the number of units you have spent "))
total=0
if unit<=100:
    total=unit*15
elif unit>100:
    total=unit*20
elif unit>=200:
    total=unit*30
print("the total bill according to the units are",total)