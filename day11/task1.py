input_file = open("input.txt")

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_string = str(stone)
            new_stones.append(int(stone_string[:len(stone_string)//2]))
            new_stones.append(int(stone_string[len(stone_string)//2:]))
        else:
            new_stones.append(2024 * stone)
    return new_stones


stones = []
for line in input_file:
    stones = [int(x) for x in line.strip().split()]

input_file.close()

for i in range(25):
    stones = blink(stones)

print(len(stones))
