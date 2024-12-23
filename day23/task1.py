input_file = open("input.txt")

neighbours = {}

for line in input_file:
    neighbour1, neighbour2 = line.strip().split("-")

    if neighbour1 not in neighbours:
        neighbours[neighbour1] = [neighbour2]
    else:
        neighbours[neighbour1].append(neighbour2)

    if neighbour2 not in neighbours:
        neighbours[neighbour2] = [neighbour1]
    else:
        neighbours[neighbour2].append(neighbour1)

input_file.close()


three_sets = set()

for computer, adjacent_computers in neighbours.items():
    if computer[0] == "t":
        for i1 in range(len(adjacent_computers) - 1):
            for i2 in range(i1 + 1, len(adjacent_computers)):
                if adjacent_computers[i1] in neighbours[adjacent_computers[i2]]:
                    three_set = tuple(sorted([computer, adjacent_computers[i1], adjacent_computers[i2]]))
                    three_sets.add(three_set)

print(len(three_sets))
