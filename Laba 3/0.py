number = [1, 3, 2, 5, 4, 7, 6]

result=[]
for i in range(1, len(number)):
    if number[i]>number[i-1]:
        result.append(number[i])
print(result)