num=int(input("entr a number you want to reverse "))
n1=0
reverse=0
while num>0:
    n1=num%10
    reverse=reverse*10+n1
    num//=10
print("the reverse number is ",reverse)
