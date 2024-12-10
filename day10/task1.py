input_file = open("input.txt")

def find_trailhead_score(topographic_map, trailhead_coords):
    if topographic_map[trailhead_coords[0]][trailhead_coords[1]] != 0:
        raise Exception("Not a trailhead!")
    positions = [trailhead_coords]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for next_value in range(1, 10):
        new_positions = []
        for position in positions:
            for direction in directions:
                new_position = (position[0] + direction[0], position[1] + direction[1])
                if new_position[0] in range(len(topographic_map)) and new_position[1] in range(len(topographic_map[0])):
                    if topographic_map[new_position[0]][new_position[1]] == next_value:
                        if new_position not in new_positions:
                            new_positions.append(new_position)
        positions = new_positions

    return len(positions)


topographic_map = []
trailheads = []

for line in input_file:
    row = [int(x) for x in list(line.strip())]
    for i, element in enumerate(row):
        if element == 0:
            trailheads.append((len(topographic_map), i))
    topographic_map.append(row)

input_file.close()

s = 0
for trailhead in trailheads:
    s += find_trailhead_score(topographic_map, trailhead)

print(s)
