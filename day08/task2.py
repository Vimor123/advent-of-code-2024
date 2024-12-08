input_file = open("input.txt")


def coords_for_antinodes(constraints, antenna1, antenna2):
    antenna_vector = (antenna2[0] - antenna1[0], antenna2[1] - antenna1[1])
    coords_group = [antenna1]
    exited1 = False
    while not exited1:
        new_coords1 = (coords_group[-1][0] - antenna_vector[0], coords_group[-1][1] - antenna_vector[1])
        if new_coords1[0] in range(constraints[0]) and new_coords1[1] in range(constraints[1]):
            coords_group.append(new_coords1)
        else:
            exited1 = True

    coords_group.append(antenna2)
    exited2 = False
    while not exited2:
        new_coords2 = (coords_group[-1][0] + antenna_vector[0], coords_group[-1][1] + antenna_vector[1])
        if new_coords2[0] in range(constraints[0]) and new_coords2[1] in range(constraints[1]):
            coords_group.append(new_coords2)
        else:
            exited2 = True
    
    return coords_group


antenna_map = []
antennas = {}

for line in input_file:
    elements = list(line.strip())
    for i in range(len(elements)):
        if elements[i] != ".":
            if elements[i] in antennas:
                antennas[elements[i]].append((len(antenna_map), i))
            else:
                antennas[elements[i]] = [(len(antenna_map), i)]
    antenna_map.append(elements)

input_file.close()


antinodes = set()

for element in antennas:
    specific_antennas = antennas[element]
    for i in range(len(specific_antennas) - 1):
        for j in range(i + 1, len(specific_antennas)):
            possible_antinodes = coords_for_antinodes((len(antenna_map), len(antenna_map[0])), specific_antennas[i], specific_antennas[j])
            for possible_antinode in possible_antinodes:
                antinodes.add(possible_antinode)

print(len(antinodes))
