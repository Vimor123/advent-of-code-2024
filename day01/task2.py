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

def search_ys(element, i, ys):
    searching = True
    count = 0
    last_index = i
    while searching:
        if i >= len(ys) - 1:
            return 0, i
        elif element > ys[i]:
            i += 1
        elif element == ys[i]:
            count += 1
            i += 1
        else:
            last_index = i
            searching = False
    return count, last_index

s = 0
current_ys_i = 0
current_x_count = 0
for i in range(len(xs)):
    if i <= len(xs) - 1 or xs[i + 1] != xs[i]:
        current_x_count += 1
        count, current_ys_i = search_ys(xs[i], current_ys_i, ys)
        s += count * xs[i]
        current_x_count = 0
    else:
        current_x_count += 1

print(s)

