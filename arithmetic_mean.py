def calculate_arithmetic_mean(file_path):
    # Open the file
    with open(file_path, 'r') as file:
        # Read the numbers from the file
        numbers = [float(line.strip()) for line in file]

    # Calculate the sum of the numbers
    # I could use the built-in sum function, but I'll use a for loop to show another way to calculate the sum
    total = 0
    for number in numbers:
        total += number

    # Calculate the length of the list
    count = len(numbers)

    # Calculate the arithmetic mean
    mean = total / count

    # Return the arithmetic mean
    return mean

file_path = '10m.txt'
result = calculate_arithmetic_mean(file_path)
print(f"The arithmetic mean is: {result}")