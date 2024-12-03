import re

input_file = open("input.txt")

s = 0
multiplying = True
for line in input_file:
    x = re.findall(r'(mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\))', line)
    for i in range(len(x)):
        if x[i] == "do()":
            multiplying = True
        elif x[i] == "don't()":
            multiplying = False
        elif multiplying:
            a, b = [int(number) for number in x[i][4:-1].split(',')]
            s += a * b

input_file.close()

print(s)
