year = int(input())
zodiak = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]

animal = zodiak[year % 12]
print(animal)