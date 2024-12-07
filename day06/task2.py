input_file = open("input.txt")

lab_map = []
position = [0, 0]
direction_index = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_symbols = ["^", ">", "v", "<"]


def possible_obstruction(lab_map, position, direction_index, optional_box_position = None):
    new_lab_map = []
    for i in range(len(lab_map)):
        new_lab_map.append(lab_map[i].copy())
    new_position = position.copy()
    if optional_box_position is None:
        box_position = [new_position[0] + directions[direction_index][0],
                        new_position[1] + directions[direction_index][1]]
    else:
        box_position = optional_box_position
    new_lab_map[box_position[0]][box_position[1]] = "#"

    hit = False
    loop = False
    while not hit:
        new_new_position = new_position.copy()
        new_new_position[0] += directions[direction_index][0]
        new_new_position[1] += directions[direction_index][1]

        if new_new_position[0] not in range(len(new_lab_map)) or new_new_position[1] not in range(len(new_lab_map[new_new_position[0]])):
            hit = True
            continue

        if new_lab_map[new_new_position[0]][new_new_position[1]] == "#":
            direction_index += 1
            direction_index %= len(directions)

        else:
            if new_lab_map[new_new_position[0]][new_new_position[1]] == direction_symbols[direction_index]:
                hit = True
                loop = True
            else:
                new_lab_map[new_new_position[0]][new_new_position[1]] = direction_symbols[direction_index]
                new_position = new_new_position

    return loop


for line in input_file:
    new_row = list(line.strip())
    if "^" in new_row:
        position = [len(lab_map), new_row.index("^")]
        starting_tuple = (len(lab_map), new_row.index("^"))
    lab_map.append(new_row)

input_file.close()

lab_map[position[0]][position[1]] = "."

possible_boxes = set()
for i in range(len(lab_map)):
    for j in range(len(lab_map[i])):
        if lab_map[i][j] == ".":
            if possible_obstruction(lab_map, position, 0, [i, j]):
                possible_boxes.add((i, j))

print(len(possible_boxes))
