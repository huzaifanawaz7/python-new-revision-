num=int(input("enter a number you want to find the sum "))
sum=0
n1=0
while num>0:
    n1=num%10
    sum+=n1
    num//=10
print("so the sum of digits of the numver is ",sum)