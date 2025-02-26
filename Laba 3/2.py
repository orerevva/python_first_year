s1 = [4, 5, 6, 7, 2, 1]
s2 = [1, 8, 6, 9, 2]

c = 0
for n in s1:
    if n in s2:
        c += 1
print(c)