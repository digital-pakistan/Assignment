# Write a program that checks if a given number is positive, negative, or zero.
def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

# Input from the user
try:
    user_input = float(input("Enter a number: "))
    result = check_number(user_input)
    print(result)
except ValueError:
    print("Please enter a valid number.")
