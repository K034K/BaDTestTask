def find_max_value(file_path):
    # reading the file and storing the numbers in a list
    with open(file_path, 'r') as file:
        numbers = [int(line) for line in file]
    
    # setting the first number as the maximum value
    max_value = numbers[0]

    # iterating through the list of numbers
    for number in numbers:
        if number > max_value:
            max_value = number

    # returning the maximum value
    return max_value

# calling the function and printing the maximum value
file_path = '10m.txt'
max_value = find_max_value(file_path)
print(f"The maximum value is: {max_value}")