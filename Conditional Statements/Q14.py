# Check if a year input by the user is a century year.
def is_century_year(year):
    return year % 100 == 0 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0

year = int(input("Enter a year: "))

if is_century_year(year):
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")
