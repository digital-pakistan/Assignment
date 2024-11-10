# Write a program to find the largest of two numbers.
def find_largest(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal."

# Input from the user
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    largest = find_largest(number1, number2)
    if isinstance(largest, str):
        print(largest)
    else:
        print(f"The largest number is: {largest}")
except ValueError:
    print("Please enter valid numbers.")
