import random
def generate_ip():
    numbers = range(255)
    n = random.sample(numbers, 4)
    k = [str(i) for i in n]
    return ".".join(k)