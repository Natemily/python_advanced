word = input()
d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
count = 0
for i in word:
    for k, v in d.items():
        if i in v:
            count += k
print(count)
