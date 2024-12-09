input_file = open("input.txt")

dense_format_string = ""
for line in input_file:
    dense_format_string = line.strip()

input_file.close()

files = {}
reading_file = True
file_index = 0
space_index = 0
holes = {}
for character in dense_format_string:
    if reading_file:
        files[file_index] = (space_index, space_index + int(character) - 1)
        space_index += int(character)
        file_index += 1
    elif int(character) != 0:
        holes[(file_index - 1, file_index)] = (space_index, space_index + int(character) - 1)
        space_index += int(character)
    reading_file = not reading_file

file_indexes = list(files.keys())
file_indexes.pop(0)

hole_markers = list(holes.keys())

space_index = files[0][1] + 1

for i in range(len(file_indexes) - 1, -1, -1):
    file_index = file_indexes[i]
    file_range = files[file_index]
    file_range_size = file_range[1] - file_range[0] + 1
    for i in range(len(hole_markers)):
        hole_range = holes[hole_markers[i]]
        hole_range_size = hole_range[1] - hole_range[0] + 1
        if hole_range_size >= file_range_size:
            hole_marker = hole_markers[i]
            files[file_index] = (hole_range[0], hole_range[0] + file_range[1] - file_range[0])
            if hole_range_size == file_range_size:
                hole_markers.pop(i)
                holes.pop(hole_marker)
            else:
                holes.pop(hole_marker)
                hole_markers[i] = (file_index, hole_marker[1])
                holes[hole_markers[i]] = (hole_range[0] + file_range[1] - file_range[0] + 1, hole_range[1])

            break

    holes_cleaned = False
    while not holes_cleaned:
        holes_cleaned = True
        for i in range(len(hole_markers)):
            if hole_markers[i][1] == file_index:
                holes_cleaned = False
                holes.pop(hole_markers[i])
                hole_markers.pop(i)
                break

s = 0
for file, file_range in files.items():
    for i in range(file_range[0], file_range[1] + 1):
        s += file * i
print(s)
