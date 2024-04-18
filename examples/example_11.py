# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Check if the input string is empty
if len(input_string) == 0:
    print(0)  # If the string is empty, print 0
else:
    word_count = 1  # Initialize the word count to 1
    for char in input_string:
        if char == " ":
            word_count += 1  # Increment the word count for each space character

    print(word_count)  # Print the final word count
