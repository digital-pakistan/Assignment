# Check if a given number is a multiple of both 3 and 5.
def is_multiple_of_3_and_5(num):
    return num % 3 == 0 and num % 5 == 0

# Input from the user
try:
    user_input = int(input("Enter a number: "))
    if is_multiple_of_3_and_5(user_input):
        print(f"{user_input} is a multiple of both 3 and 5.")
    else:
        print(f"{user_input} is not a multiple of both 3 and 5.")
except ValueError:
    print("Please enter a valid integer.")
