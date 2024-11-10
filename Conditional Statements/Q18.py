# Take a user’s score and determine if they pass or fail (pass if 50 or above).
# Pass/Fail Checker

def check_pass_fail(score):
    """
    Check if a score is passing or failing.

    Args:
        score (float): The score to check.

    Returns:
        str: The pass/fail status of the score.
    """
    if score >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    # Get user input
    score = float(input("Enter your score: "))

    # Check pass/fail status
    result = check_pass_fail(score)

    # Print the result
    print(f"Your score is {score}. You {result}.")

if __name__ == "__main__":
    main()

# Pass/Fail Checker

def main():
    # Get user input
    score = float(input("Enter your score: "))

    # Check pass/fail status
    print(f"Your score is {score}. You {'Pass' if score >= 50 else 'Fail'}.")

if __name__ == "__main__":
    main()
