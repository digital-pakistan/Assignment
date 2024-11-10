# Write a program to check if a number is within a specified range.
def is_in_range(num, lower, upper):
    return lower <= num <= upper

num = int(input("Enter a number: "))
lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))

if is_in_range(num, lower, upper):
    print(f"{num} is within the range [{lower}, {upper}].")
else:
    print(f"{num} is not within the range [{lower}, {upper}].")

num = int(input("Enter a number: "))
lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))

print(f"{num} is {'within' if lower <= num <= upper else 'not within'} the range [{lower}, {upper}].")
