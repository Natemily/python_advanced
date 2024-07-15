secret_word = input()
letter_dict = {}
for letter in secret_word:
    letter_dict[letter] = letter_dict.get(letter, 0) + 1
desh = {int(i): j for j, i in (input().split(": ") for _ in range(int(input())))}
for i in secret_word:
    print(desh[letter_dict[i]], end="")