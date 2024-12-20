input_file = open("input.txt")

def find_minimal_path(maze, start_position, end_position):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    positions = [(start_position, 0)]
    visited_positions = {}

    reached_end = False
    while not reached_end:
        if len(positions) < 1:
            raise Exception("End impossible to reach!")
        position, moves = positions.pop(0)
        visited_positions[position] = moves
        for direction in directions:
            new_position = (position[0] + direction[0], position[1] + direction[1])
            if maze[new_position[0]][new_position[1]] == ".":
                if new_position == end_position:
                    reached_end = True
                    visited_positions[end_position] = moves + 1
                if new_position not in visited_positions:
                    if (new_position, moves + 1) not in positions:
                        positions.append((new_position, moves + 1))

    return visited_positions


maze = []
start_position = (0, 0)
end_position = (0, 0)

for line in input_file:
    row = list(line.strip())
    for i in range(len(row)):
        if row[i] == "S":
            start_position = (len(maze), i)
            row[i] = "."
        if row[i] == "E":
            end_position = (len(maze), i)
            row[i] = "."
    maze.append(row)

input_file.close()

visited_positions = find_minimal_path(maze, start_position, end_position)

visited_positions_list = []
for visited_position, moves in visited_positions.items():
    visited_positions_list.append((visited_position, moves))

visited_positions_list = sorted(visited_positions_list, key = lambda x : x[1])


saved_count = {}
for start_index in range(len(visited_positions_list) - 1):
    for end_index in range(start_index + 1, len(visited_positions_list)):
        start_position = visited_positions_list[start_index][0]
        start_moves = visited_positions_list[start_index][1]
        end_position = visited_positions_list[end_index][0]
        end_moves = visited_positions_list[end_index][1]

        distance = abs(start_position[0] - end_position[0]) + abs(start_position[1] - end_position[1])

        if distance < 21:
            old_distance = end_moves - start_moves
            saved = old_distance - distance
            if saved > 0:
                if saved in saved_count:
                    saved_count[saved] += 1
                else:
                    saved_count[saved] = 1

saved_count_keys_list = list(saved_count.keys())
saved_count_keys_list = sorted(saved_count_keys_list)

s = 0
for saved in saved_count_keys_list:
    if saved >= 100:
        s += saved_count[saved]

print(s)
