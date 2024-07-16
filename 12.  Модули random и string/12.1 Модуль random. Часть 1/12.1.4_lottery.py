import random
n = set()
while len(n) < 7:
    n.add(random.randint(1, 49))
print(*sorted(n))