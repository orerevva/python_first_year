with open('input.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))
    result = 1
    for i in numbers:
        result *= i
with open('output.txt', 'w') as f:
    f.write(str(result))
    
