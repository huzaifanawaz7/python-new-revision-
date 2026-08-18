# a=10
# int(a)
# print(type(a))
# a=10.0
# float(a)
# print(type(a))
# a="10"
# str(a)
# print(type(a))
# a=True
# print(type(a))
# bool(a)

# name=input("enter your naem")
# height=input("enter your height")
# age=input("enter your age")

try:
    num=int(input("enter any number"))
except ValueError:
    print("you are only allowed to enter your number")
print(f"the number you entered is {num}")