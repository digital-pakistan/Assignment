# Check if a string input is uppercase, lowercase, or a mix.
# Case Checker

def check_case(s):
    """
    Check if a string is uppercase, lowercase, or a mix.

    Args:
        s (str): The string to check.

    Returns:
        str: The case status of the string.
    """
    if s.isupper():
        return "Uppercase"
    elif s.islower():
        return "Lowercase"
    else:
        return "Mix"

def main():
    # Get user input
    s = input("Enter a string: ")

    # Check case status
    result = check_case(s)

    # Print the result
    print(f"The string '{s}' is {result}.")

if __name__ == "__main__":
    main()



# Case Checker

def main():
    # Get user input
    s = input("Enter a string: ")

    # Check case status
    print(f"The string '{s}' is {'Uppercase' if s.isupper() else 'Lowercase' if s.islower() else 'Mix'}.")

if __name__ == "__main__":
    main()
