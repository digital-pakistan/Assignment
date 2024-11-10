# Write a program to print the first 10 Fibonacci numbers.
# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Print the first 10 Fibonacci numbers
print("The first 10 Fibonacci numbers are:")
for _ in range(10):
    print(a)
    a, b = b, a + b  # Update a and b to the next Fibonacci numbers
