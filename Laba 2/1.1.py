def new_string(s):
    result = ""
    i = 0

    while i < len(s):
        sb = s[i]
        i += 1
        c = ""
        while i < len(s) and s[i].isdigit():
            c += s[i]
            i += 1
        if c:
            c = int(c)
        else: 
            c = 1

        result += sb*c
    return result

n = input()
print(new_string(n))
        