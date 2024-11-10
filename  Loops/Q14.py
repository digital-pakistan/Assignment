# Write a program that breaks the loop when a certain condition is met.
# Initialize a variable to store user input
number = None

# Loop until the user enters 0
while True:
    number = int(input("Enter a number (enter 0 to break the loop): "))
    
    if number == 0:  # Check the condition to break the loop
        print("You entered 0. Breaking the loop.")
        break  # Exit the loop
    
    print(f"You entered: {number}")

# Program ends here
print("Loop has been exited.")
