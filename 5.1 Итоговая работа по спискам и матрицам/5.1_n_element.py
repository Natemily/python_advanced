line, n = input().split(), int(input())
res = []
for i in range(n):
    res.append(line[i::n])
print(res)