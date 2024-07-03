n, m, max = int(input()), int(input()), -10**10
ij_list = []
matrix =[input().split() for j in range(n)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if int(matrix[i][j]) > max:
            max = int(matrix[i][j])
            ij_list = []
            ij_list.append(i)
            ij_list.append(j)
print(*ij_list)