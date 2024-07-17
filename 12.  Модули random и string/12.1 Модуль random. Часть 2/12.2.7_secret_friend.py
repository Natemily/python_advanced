import random
list = [input() for i in range(int(input()))]
friends = list.copy()
random.shuffle(friends)
count = 0
while count < len(list):
    for i in range(len(list)):
        if list[i] != friends[i]:
            count += 1
    if count < len(list):
        random.shuffle(friends)
        count = 0
for i in range(len(list)):
    print(f"{list[i]} - {friends[i]}")
