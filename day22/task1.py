input_file = open("input.txt")

prune_value = 16777216

def new_secret_number(secret_number):
    new_secret_number = secret_number * 64
    new_secret_number ^= secret_number
    new_secret_number %= prune_value

    res2 = new_secret_number // 32
    new_secret_number ^= res2
    new_secret_number %= prune_value

    res3 = new_secret_number * 2048
    new_secret_number ^= res3
    new_secret_number %= prune_value

    return new_secret_number


seeds = []

for line in input_file:
    seeds.append(int(line.strip()))

input_file.close()

s = 0
for seed in seeds:
    new_seed = seed
    for i in range(2000):
        new_seed = new_secret_number(new_seed)
    s += new_seed

print(s)
