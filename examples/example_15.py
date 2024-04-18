# Get input from the user
n = int(input("Enter the number: "))  

# Initialize the total variable
total = 0  
# Initialize the output string
output = ""  

# Check if the input is valid
# Check if the input is valid
if n >= 2:  
    for i in range(1, n):  # Iterate from 1 to n-1
        total += i * (i + 1)  # Calculate the sum of i*(i+1)
        output += f"{i}*{i + 1}+"  # Build the output string

    output = output[:-1]  # Remove the last "+" from the output string
    output += f"={total}"  # Append the total to the output string
    print(output)  # Print the final output
else:
    print("Invalid input")  # Print an error message if the input is invalid