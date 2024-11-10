# Take an integer and check if it’s even or odd.
def check_even_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

# Input from the user
try:
    user_input = int(input("Enter an integer: "))
    result = check_even_odd(user_input)
    print(result)
except ValueError:
    print("Please enter a valid integer.")
