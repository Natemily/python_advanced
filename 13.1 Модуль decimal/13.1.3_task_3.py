from decimal import *
num = Decimal(input())
num_tuple = num.as_tuple()
maximum = max(num_tuple.digits)
if -1 < num < 1:
    min = 0
else:
    min = min(num_tuple.digits)
print(maximum+min)