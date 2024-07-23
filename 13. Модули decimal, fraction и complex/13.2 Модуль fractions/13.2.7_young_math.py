import math
from fractions import Fraction as F

def find_largest_fraction(n):
    largest_fraction = F(1, 1)
    for i in range(1, n):
        j = n - i
        if i < j and math.gcd(i, j) == 1:
            largest_fraction = F(i, j)

    return largest_fraction

n = int(input())
result = find_largest_fraction(n)
print(result)