input_file = open("input.txt")

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_index = 0
maze = []
starting_position = (0, 0)

for line in input_file:
    maze.append(list(line.strip()))
    if "S" in maze[-1]:
        starting_position = (len(maze) - 1, maze[-1].index("S"))

input_file.close()

final_score = 0
end_reached = False
positions = [(starting_position, 0, 0, False)]
visited_positions = set()

while not end_reached:
    position, score, direction_index, turned = positions.pop(0)

    # Move forward
    direction = directions[direction_index]
    new_possible_position = (position[0] + direction[0], position[1] + direction[1])
    hit = maze[new_possible_position[0]][new_possible_position[1]]
    if hit == "E":
        end_reached = True
        final_score = score + 1
    elif hit == ".":
        if new_possible_position not in visited_positions:
            positions.append((new_possible_position, score + 1, direction_index, False))
            visited_positions.add(position)

    # Turn left
    if not turned:
        direction = directions[(direction_index - 1) % 4]
        new_possible_position = (position[0] + direction[0], position[1] + direction[1])
        hit = maze[new_possible_position[0]][new_possible_position[1]]
        if hit == "." or hit == "E":
            if new_possible_position not in visited_positions:
                positions.append((position, score + 1000, (direction_index - 1) % 4, True))

    # Turn right
    if not turned:
        direction = directions[(direction_index + 1) % 4]
        new_possible_position = (position[0] + direction[0], position[1] + direction[1])
        hit = maze[new_possible_position[0]][new_possible_position[1]]
        if hit == "." or hit == "E":
            if new_possible_position not in visited_positions:
                positions.append((position, score + 1000, (direction_index + 1) % 4, True))

    positions = sorted(positions, key = lambda x : x[1])

print(final_score)
