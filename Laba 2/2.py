n = input()
n = n.replace(" ","")

ch = {}
for sb in n:
    if sb in ch:
        ch[sb] += 1
    else:
        ch[sb] = 1
sort_sb = []
for sb, c in ch.items():
    sort_sb.append((sb,c))
for i in range(len(sort_sb)):
    for j in range(i+1, len(sort_sb)):
        if sort_sb[i][1] < sort_sb[j][1]:
            sort_sb[i], sort_sb[j] = sort_sb[j], sort_sb[i]
for i in range(min(3,len(sort_sb))):
    sb,c = sort_sb[i]
    print(sb,c)






