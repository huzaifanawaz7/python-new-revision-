n1=int (input("give the value of a "))
n2=int(input("give the value of b"))
n3=int(input("give the value of c"))
d=n2**2-4*n1*n3
if n1==0:
    print("the square value cant be 0 because after this it will not be quadratic equation")
if d>0:
    print("this equation will have two real distinct roots")
elif d==0:
    print("one repeated real root")
elif d<0:
    print("complex roots")
