# Write a program to determine if a given character is a vowel or consonant.
def is_vowel(char):
    # Check if the character is a vowel
    return char.lower() in 'aeiou'

# Input from the user
user_input = input("Enter a character: ")

# Check if the input is a single character
if len(user_input) == 1 and user_input.isalpha():
    if is_vowel(user_input):
        print(f'"{user_input}" is a vowel.')
    else:
        print(f'"{user_input}" is a consonant.')
else:
    print("Please enter a single alphabetic character.")
