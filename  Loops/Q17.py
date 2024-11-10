# Write a program that continues to ask for a number until the correct number is guessed.
# Define the correct number
correct_number = 7

# Initialize a variable to store the user's guess
user_guess = None

# Loop until the user guesses the correct number
while user_guess != correct_number:
    user_guess = int(input("Guess the number (between 1 and 10): "))
    
    if user_guess < correct_number:
        print("Too low! Try again.")
    elif user_guess > correct_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number.")

# Program ends here
