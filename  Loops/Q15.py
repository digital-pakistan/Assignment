# Print the sum of even and odd numbers separately up to a given number.
# Input: Get the upper limit from the user
upper_limit = int(input("Enter a number: "))

# Initialize sums for even and odd numbers
even_sum = 0
odd_sum = 0

# Loop through numbers from 1 to the upper limit
for number in range(1, upper_limit + 1):
    if number % 2 == 0:  # Check if the number is even
        even_sum += number
    else:  # The number is odd
        odd_sum += number

# Print the results
print(f"Sum of even numbers up to {upper_limit}: {even_sum}")
print(f"Sum of odd numbers up to {upper_limit}: {odd_sum}")
