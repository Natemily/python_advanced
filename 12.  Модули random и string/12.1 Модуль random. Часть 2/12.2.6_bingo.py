import random
list = set()
while len(list) < 26:
    list.add(random.randint(1, 76))
list_new = [i for i in list]
matrix = [[None] * 5 for _ in range(5)]
count = 0
for i in range(5):
    for j in range(5):
        matrix[i][j] = list_new[count]
        count += 1
matrix[2][2] = 0
for i in matrix:
    print(*i)