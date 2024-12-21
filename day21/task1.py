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


def movements_robot(keypad, starting_position, symbol):
    movements = {"^" : 0, ">" : 0, "v" : 0, "<" : 0}
    next_location = keypad[symbol]
    movement_row = next_location[0] - starting_position[0]
    movement_column = next_location[1] - starting_position[1]
    if abs(movement_row) > 0:
        movements[direction_symbols[(movement_row // abs(movement_row), 0)]] = abs(movement_row)
    if abs(movement_column) > 0:
        movements[direction_symbols[(0, movement_column // abs(movement_column))]] = abs(movement_column)

    return movements


for code in codes:
    numeric_robot = starting_numeric
    directional_robot1 = starting_directional
    directional_robot2 = starting_directional

    shortest_path = 0

    for symbol in code:
        movements_numeric = movements_robot(numeric_keypad, numeric_robot, symbol)

        for direction_symbol, number_of_moves in movements_numeric.items():
            if number_of_moves > 0:
                movements_directional1 = movements_robot(directional_keypad, directional_robot1, direction_symbol)

                for direction_symbol1, number_of_moves1 in movements_directional1.items():
                    pass

                next_directional2_location = (0, 2)

                directional_robot1 = directional_keypad[direction_symbol]

        next_directional1_location = (0, 2)

        numeric_robot = numeric_keypad[symbol]

    print(shortest_path)
