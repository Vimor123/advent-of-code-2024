input_file = open("input.txt")

dense_format_string = ""
for line in input_file:
    dense_format_string = line.strip()

input_file.close()

files = {}
reading_file = True
file_index = 0
space_index = 0
for character in dense_format_string:
    if reading_file:
        files[file_index] = [[space_index, space_index + int(character) - 1]]
        space_index += int(character)
        file_index += 1
    else:
        space_index += int(character)
    reading_file = not reading_file

file_indexes = list(files.keys())
file_indexes.pop(0)

space_index = files[0][0][1] + 1
while len(file_indexes) > 0:
    next_index = files[file_indexes[0]][0][0]
    taken_file = file_indexes.pop(0)
    if len(file_indexes) == 0:
        files[taken_file][0] = [space_index, files[taken_file][0][1] - files[taken_file][0][0] + space_index]
    
    elif space_index < next_index:
        diff = next_index - space_index
        while diff > 0 and len(file_indexes) > 0:
            target_file = file_indexes[-1]
            uncompacted_range = files[target_file][0]
            range_size = uncompacted_range[1] - uncompacted_range[0] + 1
            if diff >= range_size:
                diff -= range_size
                files[target_file][0] = [space_index, space_index + range_size - 1]
                file_indexes.pop(-1)
                space_index += range_size
            else:
                files[target_file][0] = [uncompacted_range[0], uncompacted_range[1] - diff]
                files[target_file].append([space_index, space_index + diff - 1])
                space_index += diff
                diff = 0

    space_index = files[taken_file][0][1] + 1


s = 0
for file, ranges in files.items():
    for file_range in ranges:
        for i in range(file_range[0], file_range[1] + 1):
            s += file * i
print(s)
