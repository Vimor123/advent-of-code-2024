input_file = open("input.txt")
map_size = (101, 103)


def calculate_position(robot, map_size):
    x = (robot["p"][0] + 100 * robot["v"][0]) % map_size[0]
    y = (robot["p"][1] + 100 * robot["v"][1]) % map_size[1]
    return (x, y)


robots = []

for line in input_file:
    p_string, v_string = line.strip().split()
    p = tuple([int(x) for x in p_string[2:].split(",")])
    v = tuple([int(x) for x in v_string[2:].split(",")])
    robots.append({"p" : p, "v" : v})

input_file.close()

quadrants = [0, 0, 0, 0]
for robot in robots:
    coords = calculate_position(robot, map_size)
    if coords[0] < (map_size[0] // 2):
        if coords[1] < (map_size[1] // 2):
            quadrants[0] += 1
        elif coords[1] > ((map_size[1] - 1) // 2):
            quadrants[1] += 1
    elif coords[0] > ((map_size[0] - 1) // 2):
        if coords[1] < (map_size[1] // 2):
            quadrants[2] += 1
        elif coords[1] > ((map_size[1] - 1) // 2):
            quadrants[3] += 1

s = 1
for quadrant in quadrants:
    s *= quadrant

print(s)
