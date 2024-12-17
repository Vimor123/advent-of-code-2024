number_found = False

start = 8 ** 15
program = [2, 4, 1, 2, 7, 5, 1, 3, 4, 3, 5, 5, 0, 3, 3, 0]
increment = 0
factor = 8 ** 8
matching_last_places = 2
while not number_found:
    number_found = True
    a = start + increment * factor
    outputs = []
    while a > 0:
        output = (((a % 8) ^ 1) ^ (a // (2 ** ((a % 8) ^ 2)))) % 8
        outputs.append(output)
        a //= 8

    print(start + increment, outputs)
    if number_found:
        if outputs != program:
            number_found = False

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
