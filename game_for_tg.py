from random import choice

CARD_SUITS = ['♠️', '♥️', '♦️', '♣']
CARD_RANKS = ['2', '3', '4', '5', '6', 
              '7', '8', '9', '10', 
              'J', 'Q', 'K', 'A']

card_rank, cart_suit = choice(CARD_RANKS), choice(CARD_SUITS)

result_cart = card_rank + cart_suit

print("Доброе время суток! Выберите сложность игры от 1 (менее сложный) до 4 (самый сложный):")

answer_level = input()

if answer_level not in ['1', '2', '3', '4']:
  while answer_level not in ['1', '2', '3', '4']:
    print("Вы ввели некорректное значение! Попробуйте еще раз!")
    answer_level = input()

if answer_level == '1':
  print("Вы выбрали сложность 1 (менее сложный). Вам необходимо угадать цвет карты (черный или красный).")
  answer_color = input("Введите свой ответ. R или B:")
  if answer_color not in ['R', 'B']:
    while answer_color not in ['R', 'B']:
      print("Вы ввели некорректное значение! Попробуйте еще раз! R или B")
      answer_color = input()
  if answer_color == "R" and cart_suit in ['♦️', '♥️'] \
  or answer_color == "B" and cart_suit in ['♠️', '♣']:
    print(f'Поздравляем! Вы угадали цвет карты! Была загадана карта {result_cart}. Приходите еще!')
  else:
    print(f'Вы проиграли! Была загадана карта {result_cart}. Приходите еще! Удачи!')

if answer_level == '2':
  print("Вы выбрали сложность 2 (нормальный). Вам необходимо угадать масть карты (♠️, ♥️, ♦️, ♣).")
  answer_suit = input("Введите свой ответ:")
  if answer_suit not in CARD_SUITS:
    while answer_suit not in CARD_SUITS:
      print("Вы ввели некорректное значение! Попробуйте еще раз! ♠️, ♥️, ♦️ или ♣")
      answer_suit = input()
  if answer_suit == cart_suit:
    print(f'Поздравляем! Вы угадали масть карты! Была загадана карта {result_cart}. Приходите еще!')
  else:
    print(f'Вы проиграли! Была загадана карта {result_cart}. Приходите еще! Удачи!')

if answer_level == '3':
  print("Вы выбрали сложность 3 (сложный). Вам необходимо угадать номинал карты (1-10, J, Q, K или A).")
  answer_rank = input("Введите свой ответ:")
  if answer_rank not in CARD_RANKS:
    while answer_rank not in CARD_RANKS:
      print("Вы ввели некорректное значение! Попробуйте еще раз! 1-10, J, Q, K или A")
      answer_rank = input()
  if answer_rank == card_rank:
    print(f'Поздравляем! Вы угадали номинал карты! Была загадана карта {result_cart}. Приходите еще!')
  else:
    print(f'Вы проиграли! Была загадана карта {result_cart}. Приходите еще! Удачи!')

if answer_level == '4':
  print("Вы выбрали сложность 4 (хардкор]). Вам необходимо угадать номинал карты.")
  answer_rank = input("Введите номинал карты (1-10, J, Q, K или A):")
  if answer_rank not in CARD_RANKS:
    while answer_rank not in CARD_RANKS:
      print("Вы ввели некорректное значение! Попробуйте еще раз! 1-10, J, Q, K или A")
      answer_rank = input()
  answer_suit = input("Введите масть карты (♠️, ♥️, ♦️, ♣):")
  if answer_suit not in CARD_SUITS:
    while answer_suit not in CARD_SUITS:
      print("Вы ввели некорректное значение! Попробуйте еще раз! ♠️, ♥️, ♦️ или ♣")
      answer_suit = input()  
  if answer_rank + answer_suit == result_cart:
    print(f'Поздравляем! Вы угадали карту! Была загадана {result_cart}. Приходите еще!')
  else:
    print(f'Вы проиграли! Была загадана карта {result_cart}. Приходите еще! Удачи!')