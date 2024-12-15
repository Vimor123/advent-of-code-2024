input_file = open("input.txt")

def make_move(warehouse_map, position, move):
    direction = directions[direction_symbols.index(move)]
    if warehouse_map[position[0]][position[1]] != "@":
        raise Exception("Robot is not on position!")
    wall_or_empty_space_hit = False
    search_index = 1
    while not wall_or_empty_space_hit:
        space = warehouse_map[position[0] + search_index * direction[0]][position[1] + search_index * direction[1]]
        if space == "#":
            wall_or_empty_space_hit = True
            return
        elif space == ".":
            wall_or_empty_space_hit = True
        elif space == "O":
            search_index += 1

    for i in range(search_index, 0, -1):
        warehouse_map[position[0] + i * direction[0]][position[1] + i * direction[1]] = warehouse_map[position[0] + (i - 1) * direction[0]][position[1] + (i - 1) * direction[1]]
    
    warehouse_map[position[0]][position[1]] = "."
    position[0] += direction[0]
    position[1] += direction[1]


warehouse_map = []
moves = []
position = [0, 0]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_symbols = ["^", ">", "v", "<"]

reading_map = True

for line in input_file:
    if line.strip() == "":
        reading_map = False
    elif reading_map:
        warehouse_map.append(list(line.strip()))
        if "@" in line:
            position = [len(warehouse_map) - 1, line.index("@")]
    else:
        moves.extend(list(line.strip()))

input_file.close()

for move in moves:
    make_move(warehouse_map, position, move)

s = 0
for i in range(len(warehouse_map)):
    for j in range(len(warehouse_map[0])):
        if warehouse_map[i][j] == "O":
            gps = 100 * i + j
            s += gps
print(s)
