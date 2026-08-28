numbers=[4,8,12,7,-3,10,-8]
for i in range (7):
    if numbers[i]<0:
        print("the negative number is found the numbers is",numbers[i])
        break
else:
    print("there is no negative number found")