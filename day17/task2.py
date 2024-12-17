input_file = open("input.txt")

program = []
starting_registers = {"A" : 0, "B" : 0, "C" : 0}

for line in input_file:
    if line.startswith("Register"):
        starting_registers[line[9]] = int(line[11:].strip())
    elif line.strip() != "":
        program = [int(x) for x in line[8:].strip().split(",")]

input_file.close()

def combo(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]

number_found = False
start = 8 ** 15
increment = 0
factor = 8 ** 9
matching_last_places = 2
final_number = 0

while not number_found:
    instruction_pointer = 0
    outputs = []
    number_found = True
    registers = starting_registers.copy()
    registers["A"] = start + increment * factor

    while instruction_pointer < len(program):
        operation = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
    
        if operation == 0:
            registers["A"] = registers["A"] // (2 ** combo(operand))

        elif operation == 1:
            registers["B"] = registers["B"] ^ operand

        elif operation == 2:
            registers["B"] = combo(operand) % 8

        elif operation == 3:
            if registers["A"] != 0:
                instruction_pointer = operand
                instruction_pointer -= 2

        elif operation == 4:
            registers["B"] = registers["B"] ^ registers["C"]

        elif operation == 5:
            outputs.append(combo(operand) % 8)

        elif operation == 6:
            registers["B"] = registers["A"] // (2 ** combo(operand))

        elif operation == 7:
            registers["C"] = registers["A"] // (2 ** combo(operand))

        instruction_pointer += 2

    if number_found:
        if outputs != program:
            number_found = False
        else:
            final_number = start + increment * factor

    
    matching_last_places_now = 0
    for i in range(15, -1, -1):
        if outputs[i] == program[i]:
            matching_last_places_now += 1
        else:
            break

    if matching_last_places_now > matching_last_places:
        start = start + (increment - 1) * factor
        factor //= 8
        if factor < 1:
            factor = 1
        increment = -1
        matching_last_places = matching_last_places_now

    increment += 1

print(final_number)
