input_file = open("input.txt")

lab_map = []
position = [0, 0]
direction_index = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_symbols = ["^", ">", "v", "<"]

for line in input_file:
    new_row = list(line.strip())
    if "^" in new_row:
        position = [len(lab_map), new_row.index("^")]

    new_row = [[x] for x in new_row]
    lab_map.append(new_row)

input_file.close()

lab_map[position[0]][position[1]] = ["^"]

possible_boxes = set()
exited = False
while not exited:
    new_position = position.copy()
    new_position[0] += directions[direction_index][0]
    new_position[1] += directions[direction_index][1]

    if new_position[0] not in range(len(lab_map)) or new_position[1] not in range(len(lab_map[new_position[0]])):
        exited = True
        continue

    if lab_map[new_position[0]][new_position[1]] == ["#"]:
        direction_index += 1
        direction_index %= len(directions)
    
    else:
        possible_direction_index = (direction_index + 1) % len(directions)
        looking_for = direction_symbols[possible_direction_index]
        hit = False
        loop = False
        new_possible_position = position.copy()
        while not hit:
            new_possible_position[0] += directions[possible_direction_index][0]
            new_possible_position[1] += directions[possible_direction_index][1]
            if new_possible_position[0] not in range(len(lab_map)) or new_possible_position[1] not in range(len(lab_map[new_possible_position[0]])):
                hit = True
                continue

            if looking_for in lab_map[new_possible_position[0]][new_possible_position[1]]:
                hit = True
                loop = True
                continue
            
            if lab_map[new_possible_position[0]][new_possible_position[1]] == ["#"]:
                new_possible_position[0] -= directions[possible_direction_index][0]
                new_possible_position[1] -= directions[possible_direction_index][1]
                possible_direction_index += 1
                possible_direction_index %= len(directions)

        if loop:
            possible_boxes.add((new_position[0], new_position[1]))
            
        position = new_position
        lab_map[position[0]][position[1]].append(direction_symbols[direction_index])

print(len(possible_boxes))
