def calculate_median(file_path):
    # Open the file and read the numbers into a list
    with open(file_path, 'r') as file:
        numbers = [int(line) for line in file]

    # Sort the list in ascending order
    # This is necessary to calculate the median
    numbers.sort()

    # Calculate the length of the list
    length = len(numbers)

    # Check if the length is odd or even
    if length % 2 == 1:
        # If the length is odd, the median is the middle element
        # I use 2 division to get an integer result otherwise I would get a float that will raise an error
        median = numbers[length // 2]
    else:
        # If the length is even, the median is the average of the two middle elements
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2

    # Return the median
    return median

file_path = '10m.txt'
result = calculate_median(file_path)
print(result)