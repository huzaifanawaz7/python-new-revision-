num=[12,45,67,23,98,90]
n1=int(input("enter a number you want to find"))
for i in range(6):
    if num[i]==n1:
        print("the number is found")
        break
else:
    print("this number is not exists")

