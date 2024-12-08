input_file = open("input.txt")


def coords_for_antinodes(antenna1, antenna2):
    antenna_vector = (antenna2[0] - antenna1[0], antenna2[1] - antenna1[1])
    coords1 = (antenna1[0] - antenna_vector[0], antenna1[1] - antenna_vector[1])
    coords2 = (antenna2[0] + antenna_vector[0], antenna2[1] + antenna_vector[1])
    return [coords1, coords2]


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
            possible_antinodes = coords_for_antinodes(specific_antennas[i], specific_antennas[j])
            for possible_antinode in possible_antinodes:
                if possible_antinode[0] in range(len(antenna_map)) and possible_antinode[1] in range(len(antenna_map[possible_antinode[0]])):
                    antinodes.add(possible_antinode)

print(len(antinodes))
