import random
import string
def generate_index():
    a = string.ascii_uppercase
    res = ""
    for _ in range(2):
        res += random.choice(a)
    res += str(random.choice(range(100)))
    res += "_"
    res += str(random.choice(range(100)))
    for _ in range(2):
        res += random.choice(a)
    return res