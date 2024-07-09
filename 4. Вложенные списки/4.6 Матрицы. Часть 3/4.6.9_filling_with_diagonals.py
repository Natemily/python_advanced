n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
a, k = 0, 0
for l in range(n*m):
    for i in range(n):
        for j in range(m):
            if i + j == l:
                matrix[i][j] = a + 1
                a += 1
for row in matrix:
    print(*row)