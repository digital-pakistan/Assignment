# Use a loop to print numbers in reverse order within a given range.
# Input: Get the start and end of the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Loop to print numbers in reverse order
print(f"Numbers in reverse order from {end} to {start}:")
for number in range(end, start - 1, -1):
    print(number)
