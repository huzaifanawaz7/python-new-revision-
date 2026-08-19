num=int(input("entr a number you want to check whther it is a amstrong or not"))
orignal=num
count=0
while num>0:
   num%10
   count+=1
   num//=10
amstrong_sum=0
temp=num

while temp>0:
   n1=temp%10
   amstrong_sum+=n1**count
   temp//=10
if amstrong_sum==num:
   print("the number is an amstrong number")
else:
   print("this number is not amstrong")