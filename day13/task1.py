input_file = open("input.txt")

epsilon = 0.0000001

def find_number_of_moves(claw_machine):
    a1 = claw_machine["A"][0]
    a2 = claw_machine["A"][1]
    b1 = claw_machine["B"][0]
    b2 = claw_machine["B"][1]
    c1 = claw_machine["prize"][0]
    c2 = claw_machine["prize"][1]
    b = ((a1 * c2) - (a2 * c1)) / ((a1 * b2) - (a2 * b1))
    a = (c1 - b * b1) / a1
    return a, b


claw_machines = [{"A" : (0, 0), "B" : (0, 0), "prize" : (0, 0)}]

index = 0
for line in input_file:
    if line.startswith("Button"):
        coords_string = line[9:].strip()
        coords_list = [int(x.strip()[2:]) for x in coords_string.split(",")]
        claw_machines[index][line[7]] = tuple(coords_list)
    elif line.startswith("Prize:"):
        coords_string = line[6:].strip()
        coords_list = [int(x.strip()[2:]) for x in coords_string.split(",")]
        coords_list[0] += 10000000000000
        coords_list[1] += 10000000000000
        claw_machines[index]["prize"] = tuple(coords_list)
    else:
        claw_machines.append({"A" : (0, 0), "B" : (0, 0), "prize" : (0, 0)})
        index += 1

input_file.close()

s = 0
for claw_machine in claw_machines:
    a, b = find_number_of_moves(claw_machine)
    if a >= 0 and b >= 0:
        if abs(a - round(a)) < epsilon and abs(b - round(b)) < epsilon:
            s += 3 * round(a) + round(b)
print(s)
