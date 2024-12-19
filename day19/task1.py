input_file = open("input.txt")

towels = []
patterns = []

def can_pattern_be_made(useful_towels, pattern):
    searching_length = len(pattern)
    while searching_length > 0:
        if searching_length in useful_towels:
            if pattern[:searching_length] in useful_towels[searching_length]:
                to_the_end_of_pattern = len(pattern) - searching_length
                if to_the_end_of_pattern == 0:
                    return True
                next_pattern_possible = can_pattern_be_made(useful_towels, pattern[searching_length:])
                if next_pattern_possible:
                    return True

        searching_length -= 1
    return False


reading_towels = True
for line in input_file:
    if line.strip() == "":
        reading_towels = False
    elif reading_towels:
        towels = line.strip().split(", ")
    else:
        patterns.append(line.strip())

input_file.close()

towels = sorted(towels, key = len)

useful_towels = {}

for towel in towels:
    if not can_pattern_be_made(useful_towels, towel):
        if len(towel) in useful_towels:
            useful_towels[len(towel)].append(towel)
        else:
            useful_towels[len(towel)] = [towel]

s = 0
for pattern in patterns:
    if can_pattern_be_made(useful_towels, pattern):
        s += 1

print(s)
