numbers=[4,7,2,9,4,6]
for i in range(6):
    for j in range(6):
        if numbers[i]==numbers[j]:
            if i==j:
                continue
            print("this array contain the duplicates")
else:
    print("this array does't contain the duplicates")