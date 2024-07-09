k = input().split()
n, m = int(k[0]), int(k[1])
matrix = [['.' if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0 else '*' for i in range(m)] for j in range(n)]
for row in matrix:
    print(*row)
