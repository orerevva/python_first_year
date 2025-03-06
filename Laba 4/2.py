dict_1 = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
dict_2 = {'beep' : 'car'}
dict_3 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}

vl = input()

for key, value in dict_1.items():
    if vl == value:
        print(key)

vl = input()

for key, value in dict_2.items():
    if vl == value:
        print(key)

vl = int(input())

for key, value in dict_3.items():
    if vl == value:
        print(key)