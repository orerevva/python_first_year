with open('input_3.txt', encoding='utf-8') as f:
    children = [line.strip().split() for line in f.readlines()]

children = [(child[0], child[1], int(child[2])) for child in children]

y = min(children,key=lambda x: x[2])
o = max(children,key=lambda x: x[2])

with open('y_3.txt', 'w') as f:
    f.write(f"{y[0]} {y[1]} {y[2]}")

with open('o_3.txt', 'w') as f:
    f.write(f"{o[0]} {o[1]} {o[2]}")
