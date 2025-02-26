s2 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
s3 = ['aaa', 'bbb', 'ccc']
s1 = ['abc', 'abc', 'abc']

result = {}
for s in s1:
    if s in result:
        result[s] += 1
    else:
        result[s] = 1

for s in s1:
    if s in result:
        print(result[s], end = ' ')
        del result[s]
