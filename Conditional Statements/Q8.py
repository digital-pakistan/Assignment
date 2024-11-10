# Create a program that checks if a given string is a palindrome.
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = ''.join(s.split()).lower()
    # Check if the cleaned string is the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]

# Input from the user
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
