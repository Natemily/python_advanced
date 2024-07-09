n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
a = 0
for i in range(n):
    for j in range(m):
        matrix[i][j] = a + 1
        a += 1
for i in range (len(matrix)):
    if i % 2 != 0:
        matrix[i].reverse()
        print(*matrix[i])
    else:
        print(*matrix[i])