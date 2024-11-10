# Take three sides of a triangle as input and check if they form a valid triangle.
def is_valid_triangle(a, b, c):
    # A triangle is valid if the sum of any two sides is greater than the third side
    return (a + b > c) and (a + c > b) and (b + c > a)

# Input from the user
try:
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))
    
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Please enter positive values for the sides.")
    else:
        if is_valid_triangle(side1, side2, side3):
            print("The sides form a valid triangle.")
        else:
            print("The sides do not form a valid triangle.")
except ValueError:
    print("Please enter valid numbers for the sides.")
