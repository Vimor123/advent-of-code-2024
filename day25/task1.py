input_file = open("input.txt")

keys = []
locks = []

hashtags_per_column = [-1, -1, -1, -1, -1]
reading = "Unknown"
for line in input_file:
    if line.strip() == "":
        if reading == "Lock":
            locks.append(tuple(hashtags_per_column))
        elif reading == "Key":
            keys.append(tuple(hashtags_per_column))
        reading = "Unknown"
        hashtags_per_column = [-1, -1, -1, -1, -1]
    else:
        if reading == "Unknown":
            if line[0] == "#":
                reading = "Lock"
            else:
                reading = "Key"
        for i in range(5):
            if line[i] == "#":
                hashtags_per_column[i] += 1

input_file.close()

if reading == "Lock":
    locks.append(tuple(hashtags_per_column))
elif reading == "Key":
    keys.append(tuple(hashtags_per_column))


s = 0
for key in keys:
    for lock in locks:
        fit = True
        for i in range(5):
            if key[i] + lock[i] > 5:
                fit = False
        if fit:
            s += 1

print(s)
