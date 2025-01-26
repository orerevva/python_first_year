a = int(input())

for i in range(a, 0, -1):
    sp = ' ' * (a - i)
    st = sp
    for j in range(i, 0, -1):
        st += str(j)
    for j in range(2, i+1):
        st += str(j)

    print(st)