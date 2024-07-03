n, m = int(input()), int(input())
matrix =[input().split() for i in range(n)]
k = [int(i) for i in input().split()]
for i in range(n):
    matrix[i][k[0]], matrix[i][k[1]] = matrix[i][k[1]], matrix[i][k[0]]
    print(*matrix[i])