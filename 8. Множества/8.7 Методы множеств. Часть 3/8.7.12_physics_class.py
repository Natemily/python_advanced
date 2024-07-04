st1, st2, st3 = set(int(i) for i in input().split()), set(int(i) for i in input().split()), set(int(i) for i in input().split())
print(*sorted(st3 - st2 - st1, reverse=True))