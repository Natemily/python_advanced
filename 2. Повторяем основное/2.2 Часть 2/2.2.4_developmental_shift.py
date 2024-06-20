line = input().split()
line2 = [line[-1]]
for i in range(0, len(line) - 1):
    line2.append(line[i])
print(*line2)