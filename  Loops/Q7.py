# Find the factorial of a number using a while loop.
# Input: Get the number from the user
number = int(input("Enter a number to find its factorial: "))

# Initialize variables
factorial = 1
count = 1

# Calculate factorial using a while loop
while count <= number:
    factorial *= count  # Multiply the current count to the factorial
    count += 1  # Increment the count

# Print the result
print(f"The factorial of {number} is: {factorial}")
