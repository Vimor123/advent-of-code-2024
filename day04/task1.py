input_file = open("input.txt")

def find_all_xmases_for_position(matrix, coords):
    if matrix[coords[0]][coords[1]] != "X":
        return 0

    word = "XMAS"
    count = 0
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), 
                  (1, 0), (1, -1), (0, -1), (-1, -1)]
    for direction in directions:
        xmas_found = True
        new_coords = coords.copy()
        for letter_index in range(1, len(word)):
            new_coords[0] += direction[0]
            new_coords[1] += direction[1]
            if new_coords[0] in range(len(matrix)) and new_coords[1] in range(len(matrix[new_coords[0]])):
                if matrix[new_coords[0]][new_coords[1]] != word[letter_index]:
                    xmas_found = False
            else:
                xmas_found = False
        if xmas_found:
            count += 1

    return count


word_search = []
for line in input_file:
    word_search.append(line.strip())

input_file.close()

s = 0
for i in range(len(word_search)):
    for j in range(len(word_search[i])):
        s += find_all_xmases_for_position(word_search, [i, j])

print(s)
