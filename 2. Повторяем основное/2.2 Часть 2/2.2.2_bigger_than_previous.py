line = input().split()
count = 0
for i in range(1, len(line)):
    if int(line[i-1]) < int(line[i]):
        count += 1
print(count)