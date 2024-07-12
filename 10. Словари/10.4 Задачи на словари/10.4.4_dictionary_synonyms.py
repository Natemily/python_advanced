dict = {i: j for i, j in (input().split() for _ in range(int(input())))}
word = input()
if word in dict:
    print(dict[word])
else:
    for key, value in dict.items():
        if word == value:
            print(key)
