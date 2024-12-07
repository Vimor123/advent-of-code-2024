input_file = open("input.txt")

def equation_possible(equation):
    goal = equation["result"]
    elements = equation["equation"]

    possible_equations = equation_possible_rec(equation, len(elements) - 1)
    if goal in possible_equations:
        return True
    return False


def equation_possible_rec(equation, current_index):
    goal = equation["result"]
    elements = equation["equation"]
    if current_index == 0:
        return [elements[0]]

    possible_equations = equation_possible_rec(equation, current_index - 1)
    new_possible_equations = []
    for possible_equation in possible_equations:
        result1 = possible_equation * elements[current_index]
        if result1 <= goal:
            new_possible_equations.append(result1)
        result2 = possible_equation + elements[current_index]
        if result2 <= goal:
            new_possible_equations.append(result2)

    return new_possible_equations


equations = []
for line in input_file:
    result, rest = line.strip().split(":")
    result = int(result)
    rest = [int(x) for x in rest.strip().split()]
    equations.append({"result" : result, "equation" : rest})

input_file.close()

s = 0
for equation in equations:
    if equation_possible(equation):
        s += equation["result"]
print(s)
