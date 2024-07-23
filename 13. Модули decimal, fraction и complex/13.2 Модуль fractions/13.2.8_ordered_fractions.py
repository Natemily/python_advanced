import math
from fractions import Fraction as F


s = []
def find_irreducible_fractions(n):
    for denominator in range(2, n + 1):
        for numerator in range(1, denominator):
            if math.gcd(numerator, denominator) == 1:
                s.append(F(numerator, denominator))

n = int(input())
find_irreducible_fractions(n)
s = sorted(s)
for i in s:
    print(i, end="\n")