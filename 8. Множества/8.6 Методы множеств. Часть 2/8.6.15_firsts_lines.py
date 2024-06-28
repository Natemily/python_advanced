a, b = set(int(i) for i in input().split()), set(int(i) for i in input().split())
a -= b
a_sorted = sorted(a)
print(*a_sorted)