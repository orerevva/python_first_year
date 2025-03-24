with open('input_2.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f.readlines()]

    numbers.sort()

with open('output_2.txt', 'w') as f:
    f.write('\n'.join(map(str,numbers)))