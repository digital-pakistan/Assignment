# Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.
# Divisibility Checker

def check_divisibility(num):
    """
    Check if a number is divisible by 2, 3, or both.

    Args:
        num (int): The number to check.

    Returns:
        str: The divisibility status of the number.
    """
    if num % 2 == 0 and num % 3 == 0:
        return "Divisible by both 2 and 3"
    elif num % 2 == 0:
        return "Divisible by 2"
    elif num % 3 == 0:
        return "Divisible by 3"
    else:
        return "Not divisible by either 2 or 3"

def main():
    # Get user input
    num = int(input("Enter an integer: "))

    # Check divisibility
    result = check_divisibility(num)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()

# Divisibility Checker

def main():
    # Get user input
    num = int(input("Enter an integer: "))

    # Check divisibility
    if num % 2 == 0 and num % 3 == 0:
        print("Divisible by both 2 and 3")
    elif num % 2 == 0:
        print("Divisible by 2")
    elif num % 3 == 0:
        print("Divisible by 3")
    else:
        print("Not divisible by either 2 or 3")

if __name__ == "__main__":
    main()
