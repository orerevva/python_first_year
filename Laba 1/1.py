def search_min_max(a,b,c):
    minimum = a
    maximum = a
    if b > maximum:
        maximum = b
    if b < minimum:
        minimum = b
    if c > maximum:
        maximum = c
    if c < minimum:
        minimum = c 
    return maximum, minimum

a = int(input())
b = int(input())
c = int(input())

print(search_min_max(a, b, c))