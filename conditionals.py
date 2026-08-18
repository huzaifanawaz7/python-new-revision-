# num=int(input("enter your number"))
# if num>=0:
#     print("the number is positive ")
# else:
#     print("the number is negative")
# marks=int(input("enter your marks"))
# if marks>=90:
#     print("A+")
# elif marks>=80:
#     print("B+")

# given three given sides can form a triangle
try:
    perpendicular=int(input("eter the length og th eprependicular"))
except ValueError:
    print("only numbers aer allowed")
try:
    base=int(input("eter the length og th e  base"))
except:
    print("only numbers are allowed")
try:
    hypotenous=int(input("enter the length og th e htypotenous"))
except:
    print("only numbers aer allowed")
if perpendicular**2+base**2==hypotenous**2:
    print("these are the sides of the triangle")
else:
    print("these are not the sides of the triangles")



    
