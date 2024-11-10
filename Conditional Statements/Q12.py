# Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
def temperature_category(celsius):
    if celsius <= 0:
        return "Freezing"
    elif 0 < celsius < 25:
        return "Moderate"
    else:
        return "Hot"

# Input from the user
try:
    temperature = float(input("Enter the temperature in Celsius: "))
    category = temperature_category(temperature)
    print(f"The temperature is considered: {category}.")
except ValueError:
    print("Please enter a valid number for the temperature.")
