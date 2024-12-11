input_file = open("input.txt")

def blink(stones):
    new_stones = {}
    for stone, quantity in stones.items():
        if stone == 0:
            if 1 in new_stones:
                new_stones[1] += quantity
            else:
                new_stones[1] = quantity
        elif len(str(stone)) % 2 == 0:
            stone_string = str(stone)
            if int(stone_string[:len(stone_string)//2]) in new_stones:
                new_stones[int(stone_string[:len(stone_string)//2])] += quantity
            else:
                new_stones[int(stone_string[:len(stone_string)//2])] = quantity
            if int(stone_string[len(stone_string)//2:]) in new_stones:
                new_stones[int(stone_string[len(stone_string)//2:])] += quantity
            else:
                new_stones[int(stone_string[len(stone_string)//2:])] = quantity
        else:
            if stone * 2024 in new_stones:
                new_stones[2024 * stone] += quantity
            else:
                new_stones[2024 * stone] = quantity
    return new_stones


stones_list = []
for line in input_file:
    stones_list = [int(x) for x in line.strip().split()]

input_file.close()

stones = {}

for stone in stones_list:
    if stone in stones:
        stones[stone] += 1
    else:
        stones[stone] = 1

for i in range(75):
    stones = blink(stones)

s = 0
for stone, quantity in stones.items():
    s += quantity
print(s)
