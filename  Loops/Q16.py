# Create a program to calculate the sum of the digits of an inputted integer.
# Input: Get the integer from the user
number = int(input("Enter an integer: "))

# Initialize the sum of digits
digit_sum = 0

# Handle negative numbers by taking the absolute value
number = abs(number)

# Loop to calculate the sum of the digits
while number > 0:
    digit_sum += number % 10  # Add the last digit to the sum
    number //= 10  # Remove the last digit

# Print the result
print("The sum of the digits is:", digit_sum)
