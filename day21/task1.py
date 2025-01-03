input_file = open("input2.txt")


codes = []
for line in input_file:
    codes.append(line.strip())

input_file.close()


numeric_keypad = {"7" : (0, 0), "8" : (0, 1), "9" : (0, 2),
                  "4" : (1, 0), "5" : (1, 1), "6" : (1, 2),
                  "1" : (2, 0), "2" : (2, 1), "3" : (2, 2),
                                "0" : (3, 1), "A" : (3, 2)}

starting_numeric = (3, 2)

directional_keypad = {              "^" : (0, 1), "A" : (0, 2),
                      "<" : (1, 0), "v" : (1, 1), ">" : (1, 2)}

starting_directional = (0, 2)

direction_symbols = {(0, -1) : "<",
                     (-1, 0) : "^",
                     (0, 1) : ">",
                     (1, 0) : "v"}

direction_values = {"<" : (0, -1),
                    "^" : (-1, 0),
                    ">" : (0, 1),
                    "v" : (1, 0)}


def movements_robot(keypad, starting_position, symbol):
    movements = {"^" : 0, ">" : 0, "v" : 0, "<" : 0}
    next_location = keypad[symbol]
    movement_row = next_location[0] - starting_position[0]
    movement_column = next_location[1] - starting_position[1]
    if abs(movement_row) > 0:
        movements[direction_symbols[(movement_row // abs(movement_row), 0)]] = abs(movement_row)
    if abs(movement_column) > 0:
        movements[direction_symbols[(0, movement_column // abs(movement_column))]] = abs(movement_column)

    movements_string = ""
    for movement_symbol, amount in movements.items():
        movements_string += movement_symbol * amount

    return movements_string + "A"


for code in codes:
    numeric_robot = list(starting_numeric)
    directional_robot1 = list(starting_directional)
    directional_robot2 = list(starting_directional)

    all_moves = ""
    for symbol in code:
        moves_numeric = movements_robot(numeric_keypad, numeric_robot, symbol)
        for move_numeric in moves_numeric[:-1]:
            numeric_robot[0] += direction_values[move_numeric][0]
            numeric_robot[1] += direction_values[move_numeric][1]
            
            moves_directional1 = movements_robot(directional_keypad, directional_robot1, move_numeric)
            for move_directional1 in moves_directional1[:-1]:
                directional_robot1[0] += direction_values[move_directional1][0]
                directional_robot1[1] += direction_values[move_directional1][1]

            all_moves += moves_directional1

    print(all_moves)
