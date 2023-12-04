symbols = ['-', '/', '=', '+', '$', '&', '@', '*', '%', '#']
engine_schematic_matrix = []
part_numbers = []


def symbol_checker(i, j, engine_matrix):
    adj_values = [engine_matrix[i-1][j-1], engine_matrix[i-1][j], engine_matrix[i-1][j+1],
                  engine_matrix[i+1][j-1], engine_matrix[i+1][j], engine_matrix[i+1][j+1], 
                  engine_matrix[i][j-1], engine_matrix[i][j+1]]

    adj_to_symbol = False
    for value in adj_values:
        if value in symbols:
            adj_to_symbol = True

    num_to_right = False
    if engine_matrix[i][j+1].isdigit():
        num_to_right = True
    
    return adj_to_symbol, num_to_right


with open("input.txt", "r") as input_file:
    
    for index, line in enumerate(input_file):
        line = line.strip()

        engine_schematic_matrix.append(list(line))
        engine_schematic_matrix[index].append(".")
        engine_schematic_matrix[index].insert(0, ".")

    engine_schematic_matrix.insert(0, ["."] * len(engine_schematic_matrix[0]))
    engine_schematic_matrix.append(["."] * len(engine_schematic_matrix[0]))


    for i, engine_line in enumerate(engine_schematic_matrix):

        is_engine_part = False
        engine_part_number = ""

        for j, value in enumerate(engine_line):
            
            if value.isdigit():
                adj_symbol, num_to_right = symbol_checker(i, j, engine_schematic_matrix)

                if adj_symbol:
                    is_engine_part = True
                
                engine_part_number += value

                if not num_to_right and is_engine_part:
                    part_numbers.append(int(engine_part_number))
                    is_engine_part = False
                    engine_part_number = ""
                
                elif not num_to_right and not is_engine_part:
                    engine_part_number = ""

print(sum(part_numbers))

# np.savetxt("array.txt", np.array(engine_schematic_matrix), fmt='%s')