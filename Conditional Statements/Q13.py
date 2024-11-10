# Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.
def math_operation(num1, num2, operator):
    try:
        return eval(f"{num1} {operator} {num2}")
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return str(e)

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

print(f"The result is: {math_operation(num1, num2, operator)}")
