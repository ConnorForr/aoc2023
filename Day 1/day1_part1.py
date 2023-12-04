calibration_values = []

with open('day1_input.txt', 'r') as file:
    for line in file:
        numbers = [int(value) for value in line.strip() if value.isdigit()]
        first_digit = numbers[0]
        last_digit = numbers[len(numbers) - 1]


        calibration_values.append(int(str(first_digit) + str(last_digit)))

print(sum(calibration_values))
                