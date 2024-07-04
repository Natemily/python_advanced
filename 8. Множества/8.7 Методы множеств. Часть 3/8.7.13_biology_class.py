st1, st2, st3 = set(int(i) for i in input().split()), set(int(i) for i in input().split()), set(int(i) for i in input().split())
st4 = set(range(11))
print(*sorted(st4 ^ (st3 | st2 | st1)))