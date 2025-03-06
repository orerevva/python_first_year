s = input()
dict = {}

for i in s:
    n = int(i)
    dict[n] = dict.get(n,0) + 1

sort_dict = sorted(dict.items(), key = lambda x:x[1], reverse = True)
print(sort_dict[:3])


