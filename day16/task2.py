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

final_scores = []
final_histories = []
end_reached = False
positions = [(starting_position, 0, 0, False, [starting_position])]
visited_positions = set()

while not end_reached:
    if len(positions) == 0:
        break
    position, score, direction_index, turned, history = positions.pop(0)

    if len(final_scores) > 0:
        if score >= final_scores[0]:
            end_reached = True

    # Move forward
    direction = directions[direction_index]
    new_possible_position = (position[0] + direction[0], position[1] + direction[1])
    hit = maze[new_possible_position[0]][new_possible_position[1]]
    if hit == "E":
        final_scores.append(score + 1)
        final_history = history.copy()
        final_history.append(new_possible_position)
        final_histories.append(final_history)
    elif hit == ".":
        if (new_possible_position, direction_index) not in visited_positions:
            new_history = history.copy()
            new_history.append(new_possible_position)
            positions.append((new_possible_position, score + 1, direction_index, False, new_history))
            visited_positions.add((position, direction_index))

    # Turn left
    if not turned:
        direction = directions[(direction_index - 1) % 4]
        new_possible_position = (position[0] + direction[0], position[1] + direction[1])
        hit = maze[new_possible_position[0]][new_possible_position[1]]
        if hit == "." or hit == "E":
            if (new_possible_position, (direction_index - 1) % 4) not in visited_positions:
                positions.append((position, score + 1000, (direction_index - 1) % 4, True, history))

    # Turn right
    if not turned:
        direction = directions[(direction_index + 1) % 4]
        new_possible_position = (position[0] + direction[0], position[1] + direction[1])
        hit = maze[new_possible_position[0]][new_possible_position[1]]
        if hit == "." or hit == "E":
            if (new_possible_position, (direction_index + 1) % 4) not in visited_positions:
                positions.append((position, score + 1000, (direction_index + 1) % 4, True, history))

    positions = sorted(positions, key = lambda x : x[1])

final_positions = set()
for history in final_histories:
    for position in history:
        final_positions.add(position)

print(len(final_positions))
