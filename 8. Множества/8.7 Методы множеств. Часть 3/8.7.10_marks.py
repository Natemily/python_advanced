a, b, c = input().split(), input().split(), input().split()
st1, st2, st3 = {int(i) for i in a}, {int(i) for i in b}, {int(i) for i in c}
st12 = st1.intersection(st2)
st123 = st12.difference(st3)
print(*sorted(st123, reverse=True))