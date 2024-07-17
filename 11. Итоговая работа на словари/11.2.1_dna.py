dna = input()
rnc = {"G":"C", "C":"G", "T":"A", "A":"U"}
for i in dna:
    print(rnc[i], end="")