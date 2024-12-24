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
codes = {}

for line in input_file:
    if line.strip() == "":
        reading_values = False
    elif reading_values:
        wire, value = line.strip().split(": ")
        value = int(value)
        values[wire] = value
    else:
        segments = line.strip().split()
        operand1 = min(segments[0], segments[2])
        operand2 = max(segments[0], segments[2])
        gates[segments[4]] = {"operand1" : operand1,
                              "operand2" : operand2,
                              "operation" : segments[1]}
        if operand1.startswith("x"):
            codes["{}{}{}".format(operand1, operand2, segments[1].lower())] = segments[4]

input_file.close()


code_keys = list(codes.keys())
code_keys.sort()
code_keys.reverse()
for code in code_keys:
    print(code, codes[code])

