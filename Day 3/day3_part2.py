import numpy as np

engine_schematic_matrix = []
gear_ratios = []

def top_row_check(top_row):
    total_parts = 0
    part_numbers = []
    adj_number = False 
    number = ""

    for index, value in enumerate(top_row):    
       
        if value.isdigit() and index in [2, 3, 4]:
            adj_number = True
            number += value
        
        elif value.isdigit():
            number += value
        
        elif adj_number == True and not value.isdigit():
            part_numbers.append(int(number))
            adj_number = False
            number = ""
            total_parts += 1
        
        else: 
            number = ""

    if adj_number:
        part_numbers.append(int(number))

        total_parts += 1
        adj_number = False 
        number = ""

    return total_parts, part_numbers


def bottom_row_check(bottom_row):
    total_parts = 0
    part_numbers = []
    adj_number = False 
    number = ""

    for index, value in enumerate(bottom_row):    
       
        if value.isdigit() and index in [2, 3, 4]:
            adj_number = True
            number += value
        
        elif value.isdigit():
            number += value
        
        elif adj_number == True and not value.isdigit():
            part_numbers.append(int(number))
            adj_number = False
            number = ""
            total_parts += 1
        
        else: 
            number = ""

    if adj_number:
        part_numbers.append(int(number))

        total_parts += 1
        adj_number = False 
        number = ""

    return total_parts, part_numbers

def left_row_check(left_row):
    part_numbers = []
    number = ""
    total_parts = 0
    for index, value in enumerate(left_row):
        
        if value.isdigit() and index == 2:
            number += value
            total_parts += 1
            part_numbers.append(int(number))

        elif value.isdigit():
            number += value

        else:
            number = ""

    return total_parts, part_numbers

def right_row_check(right_row):
    number = ""
    total_parts = 0
    part_numbers = []
    for index, value in enumerate(right_row):
        
        if value.isdigit() and index == 0:
            number += value
            total_parts += 1
            
        elif value.isdigit():
            number += value

        elif total_parts == 1 and number != "":
            part_numbers.append(int(number))
            number = ""

    if total_parts == 1 and number != "":
        part_numbers.append(int(number))
    
    return total_parts, part_numbers

# main gear check
def gear_check(i, j, engine_matrix):
    top_row = []
    for j_index in range(j-3, j+4):
        top_row.append(engine_matrix[i-1][j_index])

    bottom_row = []
    for j_index in range(j-3, j+4):
        bottom_row.append(engine_matrix[i+1][j_index])

    left_row = []
    for j_index in range(j-3, j):
        left_row.append(engine_matrix[i][j_index])

    right_row = []
    for j_index in range(j+1, j+4):
        right_row.append(engine_matrix[i][j_index])

    top_part_count, top_row_values = top_row_check(top_row)
    bottom_part_count, bottom_row_values = bottom_row_check(bottom_row)
    left_part_count, left_row_values = left_row_check(left_row)
    right_part_count, right_row_values = right_row_check(right_row)

    total_part_count = top_part_count + bottom_part_count + left_part_count + right_part_count

    if total_part_count == 2:

        row_values = top_row_values + bottom_row_values + left_row_values + right_row_values
        gear_ratios.append(np.prod(row_values))

# main function
with open("input.txt", "r") as input_file:
    
    for index, line in enumerate(input_file):
        line = line.strip()

        engine_schematic_matrix.append(list(line))
        engine_schematic_matrix[index].append(".")
        engine_schematic_matrix[index].insert(0, ".")

    engine_schematic_matrix.insert(0, ["."] * len(engine_schematic_matrix[0]))
    engine_schematic_matrix.append(["."] * len(engine_schematic_matrix[0]))

    for i, engine_line in enumerate(engine_schematic_matrix):
        for j, value in enumerate(engine_line):

            if value == "*":
                gear_check(i, j, engine_schematic_matrix)

print(sum(gear_ratios))