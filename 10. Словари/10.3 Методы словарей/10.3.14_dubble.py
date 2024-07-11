words_list = input().split()

words_dict = {}
for word in words_list:
    words_dict[word] = words_dict.get(word, 0) + 1
count = 1  
for i in words_list:

    if words_dict[i] == 1:
        print(i, end=" ")
    else:
        print(i+"_"+str(words_dict[i]-count), end=" ")
        count += 1