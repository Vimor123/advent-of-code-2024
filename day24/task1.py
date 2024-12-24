input_file = open("input.txt")

def get_value(wire):
    if wire in values:
        return values[wire]

    gate = gates[wire]

    operand1 = gate["operand1"]
    operand1_value = -1
    if operand1 in values:
        operand1_value = values[operand1]
    else:
        operand1_value = get_value(operand1)
    if operand1_value == -1:
        raise Exception("{} value not found".format(operand1))

    operand2 = gate["operand2"]
    operand2_value = -2
    if operand2 in values:
        operand2_value = values[operand2]
    else:
        operand2_value = get_value(operand2)
    if operand2_value == -1:
        raise Exception("{} value not found".format(operand2))

    operation = gate["operation"]
    result = -1
    if operation == "AND":
        result = operand1_value & operand2_value
    elif operation == "OR":
        result = operand1_value | operand2_value
    elif operation == "XOR":
        result = operand1_value ^ operand2_value

    if result == -1:
        raise Exception("{} value not calculated".format(wire))

    values[wire] = result
    return result


reading_values = True

values = {}
gates = {}

for line in input_file:
    if line.strip() == "":
        reading_values = False
    elif reading_values:
        wire, value = line.strip().split(": ")
        value = int(value)
        values[wire] = value
    else:
        segments = line.strip().split()
        gates[segments[4]] = {"operand1" : segments[0],
                              "operand2" : segments[2],
                              "operation" : segments[1]}

input_file.close()

significant_wires = []

for wire, gate in gates.items():
    if wire.startswith("z"):
        get_value(wire)
        significant_wires.append(wire)

significant_wires.sort()
significant_wires.reverse()

final = ""
for wire in significant_wires:
    final += str(values[wire])

s = 0
for i in range(len(final)):
    if final[i] == "1":
        s += 2 ** (len(final) - i - 1)

print(s)
