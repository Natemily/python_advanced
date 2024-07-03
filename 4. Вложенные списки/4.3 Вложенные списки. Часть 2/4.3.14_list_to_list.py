list_1, list_2, list_3 = input().split(), [[]], []
for i in range(len(list_1)):
    for j in range(len(list_1)):
        list_3 = list_1[j:i+j+1]
        if len(list_3) == i+1:
            list_2.append(list_3)
print(list_2)