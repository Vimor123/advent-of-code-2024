input_file = open("input.txt")

def find_all_xmases_for_position(matrix, coords):
    if matrix[coords[0]][coords[1]] != "A":
        return 0

    word = "MAS"
    directions = [(-1, 1), (-1, -1)]
    hits = 0
    for direction in directions:
        current_word = ["A"]
        new_coords1 = coords.copy()
        new_coords2 = coords.copy()

        new_coords1[0] += direction[0]
        new_coords1[1] += direction[1]

        new_coords2[0] -= direction[0]
        new_coords2[1] -= direction[1]

        if new_coords1[0] in range(len(matrix)) and new_coords1[1] in range(len(matrix[new_coords1[0]])):
            current_word.insert(0, matrix[new_coords1[0]][new_coords1[1]])
        if new_coords2[0] in range(len(matrix)) and new_coords2[1] in range(len(matrix[new_coords2[0]])):
            current_word.append(matrix[new_coords2[0]][new_coords2[1]])

        current_string = "".join(current_word)
        if current_string == word or current_string[::-1] == word:
            hits += 1

    if hits == 2:
        return 1

    return 0


word_search = []
for line in input_file:
    word_search.append(line.strip())

input_file.close()

s = 0
for i in range(len(word_search)):
    for j in range(len(word_search[i])):
        s += find_all_xmases_for_position(word_search, [i, j])

print(s)
