# Use a loop to count the number of digits in an integer.
# Input: Get the integer from the user
number = int(input("Enter an integer: "))

# Initialize the count of digits
count = 0

# Use a loop to count the digits
# Handle negative numbers by taking the absolute value
number = abs(number)

if number == 0:
    count = 1  # Special case for 0

while number > 0:
    number //= 10  # Remove the last digit
    count += 1  # Increment the count

# Print the result
print("The number of digits is:", count)
