input_file = open("input.txt")

lab_map = []
position = [0, 0]
direction_index = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for line in input_file:
    new_row = list(line.strip())
    if "^" in new_row:
        position = [len(lab_map), new_row.index("^")]
    lab_map.append(new_row)

input_file.close()

lab_map[position[0]][position[1]] = "X"

exited = False
while not exited:
    new_position = position.copy()
    new_position[0] += directions[direction_index][0]
    new_position[1] += directions[direction_index][1]

    if new_position[0] not in range(len(lab_map)) or new_position[1] not in range(len(lab_map[new_position[0]])):
        exited = True
        continue

    if lab_map[new_position[0]][new_position[1]] == "#":
        direction_index += 1
        if direction_index >= len(directions):
            direction_index = 0
    else:
        position = new_position
        lab_map[position[0]][position[1]] = "X"

s = 0
for i in range(len(lab_map)):
    for j in range(len(lab_map[i])):
        if lab_map[i][j] == "X":
            s += 1

print(s)
