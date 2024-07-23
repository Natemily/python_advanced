from fractions import Fraction as F
from math import factorial as fac


n = int(input())
summ = 0
for i in range(1, n+1):
    summ += F(1, fac(i))
print(summ)