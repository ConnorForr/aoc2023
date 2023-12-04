calibration_values = []
conversion_dict = {"one": 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9,
                 "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9}

with open( 'day1_input.txt', 'r' ) as file:
    for line in file:
        
        line = line.strip()
        sub_str = ""

        numbers_in_line = []
        for letter in line:
            sub_str += letter

            for value in conversion_dict.keys():

                if sub_str.find( value ) != -1:

                    numbers_in_line.append( conversion_dict[value] ) 
                    sub_str = sub_str[ len(sub_str)-1: ]
        calibration_values.append( int( str(numbers_in_line[0]) + str(numbers_in_line[-1]) ) )

print( sum(calibration_values) )