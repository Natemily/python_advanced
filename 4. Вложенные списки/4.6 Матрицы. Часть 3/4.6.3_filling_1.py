k = input().split()
n, m = int(k[0]), int(k[1])
matrix = [[None] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = (i * m + j) + 1
for row in matrix:
    print(*row)