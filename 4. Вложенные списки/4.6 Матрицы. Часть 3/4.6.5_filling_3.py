n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    matrix[i][i] = 1
for i in range(n):
    matrix[i][n - i - 1] = 1
for row in matrix:
    print(*row)