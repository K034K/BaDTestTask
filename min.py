def find_minimum(file_path):
    # reading the file and storing the numbers in a list
    with open(file_path, 'r') as file:
        numbers = [int(line) for line in file]
    
    # setting the first number as the minimum value
    min_value = numbers[0]

    # iterating through the list of numbers
    for number in numbers:
        if number < min_value:
            min_value = number

    # returning the minimum value
    return min_value

# calling the function and printing the result
file_path = '10m.txt'
minimum = find_minimum(file_path)
print(f"The minimum value is: {minimum}")