# Use nested loops to print a pyramid pattern of *.
# Number of rows for the pyramid
rows = 5

# Outer loop for each row
for i in range(1, rows + 1):
    # Print spaces for alignment
    for j in range(rows - i):
        print(" ", end="")  # Print space without a newline
    # Print asterisks
    for k in range(2 * i - 1):
        print("*", end="")  # Print asterisk without a newline
    # Move to the next line after each row
    print()
