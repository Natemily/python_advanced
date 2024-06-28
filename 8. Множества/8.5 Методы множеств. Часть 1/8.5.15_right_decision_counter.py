import math
n = int(input())
list_gen = [input().split(": ") for _ in range(n)]
count_gen = len([list_gen[i][1] for i in range(len(list_gen)) if list_gen[i][1] == "Correct"])
set_gen = set([list_gen[i][0] for i in range(len(list_gen)) if list_gen[i][1] == "Correct"])
if len(set_gen) > 0:
    print(f"Верно решили {len(set_gen)} учащихся")
    correct_tries = count_gen * 100 / len(list_gen)
    if correct_tries % 1 < 0.5:
        correct_tries = int(correct_tries)
    else:
        correct_tries = math.ceil(correct_tries)
    print(f"Из всех попыток {correct_tries}% верных")
else:
    print("Вы можете стать первым, кто решит эту задачу")