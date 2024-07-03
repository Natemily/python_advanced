line, n = input().split(), int(input())
def chunked(line, n):
    full_list = []
    while len(line) > 1:
        full_list.append(line[:n])
        line = line[n:]
    if len(line) != 0:
        full_list.append(line)
    return full_list

print(chunked(line, n))