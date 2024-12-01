import fileinput

input_file = open("input.txt")

xs = []
ys = []

for line in input_file:
    x, y = [int(x) for x in line.split()]
    xs.append(x)
    ys.append(y)

input_file.close()

xs.sort()
ys.sort()

s = 0
for (x, y) in zip(xs, ys):
    s += abs(x - y)

print(s)

