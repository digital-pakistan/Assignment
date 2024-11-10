# Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).
# Triangle Classifier

def classify_triangle(a, b, c):
    """
    Classify a triangle based on its side lengths.

    Args:
        a (float): The length of side a.
        b (float): The length of side b.
        c (float): The length of side c.

    Returns:
        str: The classification of the triangle (equilateral, isosceles, or scalene).
    """
    # Check if the sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle"

    # Check if the triangle is equilateral
    if a == b == c:
        return "Equilateral"

    # Check if the triangle is isosceles
    if a == b or a == c or b == c:
        return "Isosceles"

    # If none of the above, the triangle is scalene
    return "Scalene"

def main():
    # Get user input
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    # Classify the triangle
    classification = classify_triangle(a, b, c)

    # Print the result
    print(f"The triangle is {classification}.")

if __name__ == "__main__":
    main()
