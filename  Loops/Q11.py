# Print the reverse of a given number.
# Input: Get the number from the user
number = int(input("Enter a number: "))

# Initialize a variable to store the reversed number
reversed_number = 0

# Handle negative numbers
is_negative = number < 0
number = abs(number)

# Reverse the number using a loop
while number > 0:
    digit = number % 10  # Get the last digit
    reversed_number = reversed_number * 10 + digit  # Build the reversed number
    number //= 10  # Remove the last digit

# If the original number was negative, make the reversed number negative
if is_negative:
    reversed_number = -reversed_number

# Print the result
print("The reverse of the given number is:", reversed_number)
