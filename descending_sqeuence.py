def longest_descending_sequence(file_path):

    # Open the file and read the numbers into a list
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    # Find the longest descending sequence
    longest_sequence = []

    current_sequence = []


    for num in numbers:
        if not current_sequence or num < current_sequence[-1]:  # Check if number is less than the last number
            current_sequence.append(num)
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = [num]

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    return longest_sequence

file_path = '10m.txt'
longest_sequence = longest_descending_sequence(file_path)
print("Longest descending sequence:", longest_sequence)
