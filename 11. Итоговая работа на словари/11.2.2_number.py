lst = input().split()
res = {}
for c in lst:
    if c in res:
        print(f'{res[c]}', end=' ')
    else:
        res[c] = res.get(c, 0) + 1
        print(f'{res[c]}', end=' ')
    res[c] = res.get(c, 0) + 1