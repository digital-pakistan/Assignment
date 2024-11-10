# Print all prime numbers between 1 and 50
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Print all prime numbers between 1 and 50
print("Prime numbers between 1 and 50:")
for number in range(1, 51):
    if is_prime(number):
        print(number)
