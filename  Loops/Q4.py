# Print the multiplication table of a given number.
# Input: Get the number from the user
number = int(input("Enter a number to print its multiplication table: "))

# Print the multiplication table
print(f"Multiplication table of {number}:")
for i in range(1, 11):  # Loop from 1 to 10
    result = number * i
    print(f"{number} x {i} = {result}")
