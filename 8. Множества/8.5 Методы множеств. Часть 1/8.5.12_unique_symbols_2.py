list2 = ""
list = [input().lower() for _ in range(int(input()))]
for i in range(len(list)):
    list2 += list[i]
print(len(set(list2)))