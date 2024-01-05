#!/usr/bin/python3
"""Pascal triangle"""
from math import factorial


def pascal_triangle(n: int):
    """Generating a pascal triangle using this formal
    n!//r! * (n - r)!
    """
    # if n is 0 or < 0
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        """using factorial equation for
               i!
          -----------
          j! * (i - j)
        using 2 as example in the loop above
              2!
            --------
            1! * (2 - 1)! which is 2 and move to next j loop
            and give use 1, 2, 1
        """
        row = [factorial(i) // (factorial(j) * factorial(i - j))
               for j in range(i + 1)]
        str(row).replace(", ", ",")
        triangle.append(row)
    return triangle
