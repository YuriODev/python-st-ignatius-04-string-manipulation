# ## Exercise 27: Run-Length Encoding - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

# **Problem:** Encode a string by replacing groups of identical characters with the character followed by its count.

# ### Input:
# - A string.

# ### Output:
# - The encoded string.

# ### Examples:

# | No. | Inputs      | Outputs   |
# | --- | ----------- | --------- |
# | 1   | aaaabbbcaa  | a4b3c1a2  |
# | 2   | abc         | a1b1c1    |
# | 3   | Hello       | H1e1l2o1  |
# | 4   | abcdabcd    | a1b1c1d1a1b1c1d1 |
# | 5   | xyzxyzxyz   | x1y1z1x1y1z1x1y1z1 |

# Prompt the user to enter a string
string = input("Enter a string: ")

# Initialize the encoded string
encoded_string = ""

# Initialize the count of the current character
count = 1

# Iterate through the string
for i in range(1, len(string)):
    # If the current character is the same as the previous character
    if string[i] == string[i - 1]:
        # Increment the count
        count += 1
    else:
        # Append the character and its count to the encoded string
        encoded_string += string[i - 1] + str(count)
        # Reset the count
        count = 1

# Append the last character and its count to the encoded string
encoded_string += string[-1] + str(count)

# Print the encoded string
print(encoded_string)