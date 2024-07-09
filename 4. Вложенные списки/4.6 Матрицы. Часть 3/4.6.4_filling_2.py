k = input().split()
n, m = int(k[0]), int(k[1])
matrix = [[0 for _ in range(m)] for _ in range(n)]
a = 0
for i in range(n):
    for j in range(m):
        matrix[i][j] = j * n + i + 1
for row in matrix:
    print(*row)