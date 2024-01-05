from math import factorial

def print_pascals_triangle(n):
    for i in range(n):
        # Calculate and print values for the row without space between digits
        row = [factorial(i) // (factorial(j) * factorial(i - j)) for j in range(i + 1)]
        print(str(row).replace(", ", ","))

# Example: Printing Pascal's Triangle up to the 5th row
print_pascals_triangle(5)

