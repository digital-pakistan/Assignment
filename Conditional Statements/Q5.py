# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).
def get_letter_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

# Input from the user
try:
    user_percentage = float(input("Enter your grade percentage: "))
    if 0 <= user_percentage <= 100:
        letter_grade = get_letter_grade(user_percentage)
        print(f"Your letter grade is: {letter_grade}")
    else:
        print("Please enter a valid percentage between 0 and 100.")
except ValueError:
    print("Please enter a valid number for the percentage.")
