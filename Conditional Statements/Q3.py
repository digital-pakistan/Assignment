# Write a program that checks if a given year is a leap year.
def is_leap_year(year):
    # A year is a leap year if it is divisible by 4,
    # but not divisible by 100, unless it is also divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input from the user
try:
    user_year = int(input("Enter a year: "))
    if user_year < 0:
        print("Please enter a valid year.")
    else:
        if is_leap_year(user_year):
            print(f"{user_year} is a leap year.")
        else:
            print(f"{user_year} is not a leap year.")
except ValueError:
    print("Please enter a valid number for the year.")

