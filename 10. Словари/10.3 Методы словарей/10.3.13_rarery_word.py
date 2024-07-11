words_list = input().replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(':', '').replace(';', '').lower().split()

words_dict = {}
for word in words_list:
    words_dict[word] = words_dict.get(word, 0) + 1

most_common = words_list[0]
for word in words_dict.keys():
    if words_dict[word] < words_dict[most_common]:
        most_common = word
    elif words_dict[word] == words_dict[most_common] and word < most_common:
        most_common = word

print(most_common)