def matrix(n=1, m=None, value=0):
    if m == None:
        m = n
    matrix = [[value for j in range(m)] for i in range(n)]
    return matrix