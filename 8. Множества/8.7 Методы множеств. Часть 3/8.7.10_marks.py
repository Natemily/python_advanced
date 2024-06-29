st1, st2, st3 = set(input()), set(input()), set(input())
st12 = st1.intersection(st2)
st123 = st12.difference(st3)
print(*sorted(st123, reverse=True))