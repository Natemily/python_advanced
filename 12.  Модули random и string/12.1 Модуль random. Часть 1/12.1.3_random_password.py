import random

length = int(input())    # длина пароля

for i in range(length):
    print(chr(random.choice([random.randint(65, 90), random.randint(97, 122)])), end="")