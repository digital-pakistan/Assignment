# Create a program that simulates a countdown timer starting from a given number down to zero.
import time

# Input: Get the starting number for the countdown from the user
start_number = int(input("Enter a number to start the countdown: "))

# Countdown loop
for number in range(start_number, -1, -1):
    print(number)
    time.sleep(1)  # Pause for 1 second

print("Countdown finished!")
