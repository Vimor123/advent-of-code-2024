input_file = open("input.txt")

program = []
registers = {"A" : 0, "B" : 0, "C" : 0}

for line in input_file:
    if line.startswith("Register"):
        registers[line[9]] = int(line[11:].strip())
    elif line.strip() != "":
        program = [int(x) for x in line[8:].strip().split(",")]

input_file.close()

instruction_pointer = 0
outputs = []


def combo(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]


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


print(",".join([str(x) for x in outputs]))
