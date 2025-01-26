a = int(input())

for i in range(a, 0, -1):
    st = ""
    for j in range(1, i + 1):
        st += str(j)
    print(st)