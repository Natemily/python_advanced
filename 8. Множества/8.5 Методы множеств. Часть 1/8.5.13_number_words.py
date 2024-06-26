line, line2 = input(), ""
symbols = ".,;:-?!"
for i in range(len(line)):
    if line[i] not in symbols:
        line2 += line[i]
my_set = set(line2.lower().split())
print(len(my_set))