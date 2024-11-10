# Take a user’s age as input and display whether they are a minor, adult, or senior citizen.
def check_age(age):
    if age < 18:
        return "You are a minor."
    elif 18 <= age < 65:
        return "You are an adult."
    else:
        return "You are a senior citizen."

# Input from the user
try:
    user_age = int(input("Enter your age: "))
    if user_age < 0:
        print("Please enter a valid age.")
    else:
        result = check_age(user_age)
        print(result)
except ValueError:
    print("Please enter a valid number for age.")
