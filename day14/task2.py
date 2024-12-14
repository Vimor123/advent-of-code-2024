input_file = open("input.txt")
map_size = (101, 103)


robots = []

for line in input_file:
    p_string, v_string = line.strip().split()
    p = [int(x) for x in p_string[2:].split(",")]
    v = tuple([int(x) for x in v_string[2:].split(",")])
    robots.append({"p" : p, "v" : v})

input_file.close()

seconds = 0
while seconds < 10000:
    space_map = []
    for i in range(map_size[1]):
        space_map.append([])
        for j in range(map_size[0]):
            space_map[-1].append(0)

    for robot in robots:
        robot["p"][0] += robot["v"][0]
        robot["p"][0] %= map_size[0]
        robot["p"][1] += robot["v"][1]
        robot["p"][1] %= map_size[1]
        space_map[robot["p"][1]][robot["p"][0]] = 255

    in_row_max = 0
    for i in range(len(space_map)):
        in_row_now = 0
        for j in range(len(space_map[0])):
            if space_map[i][j] == 255:
                in_row_now += 1
                if in_row_now > in_row_max:
                    in_row_max = in_row_now
            else:
                in_row_now = 0
    
    seconds += 1

    if in_row_max < 7:
        continue

    print(seconds)
    for i in range(len(space_map)):
        for j in range(len(space_map[0])):
            if space_map[i][j] == 0:
                print(".", end = "")
            else:
                print("X", end = "")
        print("")
    print("")
