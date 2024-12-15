input_file = open("input.txt")

def make_move(warehouse_map, position, move):
    direction = directions[direction_symbols.index(move)]
    if warehouse_map[position[0]][position[1]] != "@":
        raise Exception("Robot is not on position!")
    wall_or_empty_space_hit = False
    search_index = 1

    if direction[0] == 0:
        while not wall_or_empty_space_hit:
            space = warehouse_map[position[0] + search_index * direction[0]][position[1] + search_index * direction[1]]
            if space == "#":
                wall_or_empty_space_hit = True
                return
            elif space == ".":
                wall_or_empty_space_hit = True
            else:
                search_index += 1

        for i in range(search_index, 0, -1):
            warehouse_map[position[0] + i * direction[0]][position[1] + i * direction[1]] = warehouse_map[position[0] + (i - 1) * direction[0]][position[1] + (i - 1) * direction[1]]
    
        warehouse_map[position[0]][position[1]] = "."
        position[0] += direction[0]
        position[1] += direction[1]
    else:
        moving_indexes = [position[1]]
        moving_indexes_history = [moving_indexes.copy()]
        while not wall_or_empty_space_hit:
            all_empty = True
            new_moving_indexes = []
            for moving_index in moving_indexes:
                next_space = warehouse_map[position[0] + search_index * direction[0]][moving_index]
                if next_space == "#":
                    wall_or_empty_space_hit = True
                    return
                elif next_space == "[":
                    all_empty = False
                    if moving_index not in new_moving_indexes:
                        new_moving_indexes.append(moving_index)
                    if moving_index + 1 not in new_moving_indexes:
                        new_moving_indexes.append(moving_index + 1)
                elif next_space == "]":
                    all_empty = False
                    if moving_index - 1 not in new_moving_indexes:
                        new_moving_indexes.append(moving_index - 1)
                    if moving_index not in new_moving_indexes:
                        new_moving_indexes.append(moving_index)

            if all_empty:
                wall_or_empty_space_hit = True

            else:
                moving_indexes_history.append(new_moving_indexes.copy())
                moving_indexes = new_moving_indexes
                search_index += 1

        for i in range(search_index, 0, -1):
            for moving_index in moving_indexes_history[i - 1]:
                warehouse_map[position[0] + i * direction[0]][moving_index] = warehouse_map[position[0] + (i - 1) * direction[0]][moving_index]
            if i > 1:
                for moving_index in moving_indexes_history[i - 1]:
                    if moving_index not in moving_indexes_history[i - 2]:
                        warehouse_map[position[0] + (i - 1) * direction[0]][moving_index] = "."
            else:
                for moving_index in moving_indexes_history[i - 1]:
                    warehouse_map[position[0] + (i - 1) * direction[0]][moving_index] = "."
        
        warehouse_map[position[0]][position[1]] = "."
        position[0] += direction[0]

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
        new_row = []
        for element in line.strip():
            if element == "#":
                new_row.append("#")
                new_row.append("#")
            elif element == "O":
                new_row.append("[")
                new_row.append("]")
            elif element == ".":
                new_row.append(".")
                new_row.append(".")
            elif element == "@":
                new_row.append("@")
                new_row.append(".")

        warehouse_map.append(new_row)
        if "@" in new_row:
            position = [len(warehouse_map) - 1, new_row.index("@")]
    else:
        moves.extend(list(line.strip()))

input_file.close()

for move in moves:
    make_move(warehouse_map, position, move)

s = 0
for i in range(len(warehouse_map)):
    for j in range(len(warehouse_map[0])):
        if warehouse_map[i][j] == "[":
            gps = 100 * i + j
            s += gps
print(s)
