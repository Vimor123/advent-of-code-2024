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

largest_set = None


previous_sets = three_sets

while largest_set is None:
    next_sets = set()

    for computer_set in previous_sets:
        adjacent_computer_list = []
        for pc in computer_set:
            if len(adjacent_computer_list) == 0 or len(neighbours[pc]) < len(adjacent_computer_list):
                adjacent_computer_list = neighbours[pc]

        for possible_pc in adjacent_computer_list:
            possible = True
            for pc in computer_set:
                if possible_pc not in neighbours[pc]:
                    possible = False

            if possible:
                next_list = list(computer_set)
                next_list.append(possible_pc)
                next_set = tuple(sorted(next_list))
                next_sets.add(next_set)

    if len(next_sets) == 0:
        for computer_set in previous_sets:
            largest_set = computer_set
    
    previous_sets = next_sets

print(",".join(largest_set))
