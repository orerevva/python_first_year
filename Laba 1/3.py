a = int(input())

for i in range(a):
    row = [1]
    if i > 0:
        for j in range(1, i):
            row.append(lr[j-1] + lr[j])
        row.append(1)
    
    print(' '.join(map(str, row)).center(a * 3))
    lr = row