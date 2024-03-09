def longest_ascending_sequence(file_path):

    # Open the file and read the numbers into a list
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    # Find the longest ascending sequence
    longest_sequence = []

    # I'll use a for loop to iterate through the list of numbers
    current_sequence = []

    # The for loop iterates over each number in the list. 
    #For each number, it checks if current_sequence is empty 
    # or if the number is greater than the last number in current_sequence.
    # If either condition is true, it appends the number to current_sequence. 
    # If both conditions are false, it compares the length of current_sequence
    #  with the length of longest_sequence. If current_sequence is longer,
    #  it replaces longest_sequence with current_sequence.
    for num in numbers:
        if not current_sequence or num > current_sequence[-1]:
            current_sequence.append(num)
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence  
            current_sequence = [num]

    # If the last sequence is the longest, it will become the longest_sequence
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    return longest_sequence

file_path = '10m.txt'
longest_sequence = longest_ascending_sequence(file_path)
print("Longest ascending sequence:", longest_sequence)