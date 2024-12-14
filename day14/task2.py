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
running = True
while running:
    space_map = set()
    for robot in robots:
        robot["p"][0] += robot["v"][0]
        robot["p"][0] %= map_size[0]
        robot["p"][1] += robot["v"][1]
        robot["p"][1] %= map_size[1]
        space_map.add(tuple(robot["p"]))
    
    seconds += 1

    for i in range(map_size[1]):
        for j in range(map_size[0]):
            if (j, i) in space_map:
                print("O", end = "")
            else:
                print(".", end = "")
        print("")
    print("-" * map_size[0])

    k = input()
    if k == "q":
        running = False
