number = [1, 4, 7, 5, 3]

min_index=number.index(min(number))
max_index=number.index(max(number))
number[min_index], number[max_index] =  number[max_index], number[min_index]
print(number)