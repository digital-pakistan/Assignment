# Write a program to find the largest of three numbers.
def find_largest_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Input from the user
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))
    
    largest = find_largest_of_three(number1, number2, number3)
    print(f"The largest number is: {largest}")
except ValueError:
    print("Please enter valid numbers.")
