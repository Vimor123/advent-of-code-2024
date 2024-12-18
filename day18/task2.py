input_file = open("input.txt")

memory_map_size = 71

def find_exit(memory_map, starting_position, exit_position):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited_positions = {}
    positions = [(starting_position, 0)]

    exit_found = False
    while not exit_found:
        if len(positions) < 1:
            raise Exception("Impossible to exit!")
        position, moves = positions.pop(0)
        visited_positions[position] = moves
        for direction in directions:
            new_position = (position[0] + direction[0], position[1] + direction[1])
            if new_position[0] in range(len(memory_map)) and new_position[1] in range(len(memory_map[0])):
                if memory_map[new_position[0]][new_position[1]] != "#":
                    if new_position == exit_position:
                        exit_found = True
                        visited_positions[exit_position] = moves + 1
                    if new_position not in visited_positions:
                        if (new_position, moves + 1) not in positions:
                            positions.append((new_position, moves + 1))

    return visited_positions[exit_position]

memory_map = []
falling_bytes = []

for i in range(memory_map_size):
    memory_map.append([])
    for j in range(memory_map_size):
        memory_map[-1].append(".")

for line in input_file:
    x, y = [int(x) for x in line.strip().split(",")]
    falling_bytes.append((y, x))

input_file.close()

memory_map = []
for i in range(memory_map_size):
        memory_map.append([])
        for j in range(memory_map_size):
            memory_map[-1].append(".")

exit_possible = True
number_of_fallen_bytes = 0
while exit_possible:
    memory_map[falling_bytes[number_of_fallen_bytes][0]][falling_bytes[number_of_fallen_bytes][1]] = "#"

    number_of_fallen_bytes += 1
    
    try:
        s = find_exit(memory_map, (0, 0), (memory_map_size - 1, memory_map_size - 1))
    except:
        byte = falling_bytes[number_of_fallen_bytes - 1]
        print("{},{}".format(byte[1], byte[0]))
        exit_possible = False
