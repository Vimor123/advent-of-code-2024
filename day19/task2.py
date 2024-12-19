input_file = open("input.txt")

towels = []
patterns = []

no_of_combs = {}

def number_of_combinations_for_pattern(all_towels, pattern):
    searching_length = len(pattern)
    no_of_possibilities = 0
    if pattern in no_of_combs:
        return no_of_combs[pattern]
    while searching_length > 0:
        if searching_length in all_towels:
            if pattern[:searching_length] in all_towels[searching_length]:
                to_the_end_of_pattern = len(pattern) - searching_length
                if to_the_end_of_pattern == 0:
                    no_of_possibilities += 1
                else:
                    no_of_possibilities += number_of_combinations_for_pattern(all_towels, pattern[searching_length:])

        searching_length -= 1

    no_of_combs[pattern] = no_of_possibilities
    return no_of_possibilities


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

all_towels = {}

for towel in towels:
    if len(towel) in all_towels:
        all_towels[len(towel)].append(towel)
    else:
        all_towels[len(towel)] = [towel]

s = 0
for i in range(len(patterns)):
    pattern = patterns[i]
    s += number_of_combinations_for_pattern(all_towels, pattern)

print(s)
