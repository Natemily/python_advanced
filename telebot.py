import telebot
from random import choice
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = '8152631407:AAHacxc5q66JDhcOSKenIPwEzHvj8guUNpk'

CARD_SUITS = ['♠️', '♥️', '♦️', '♣']
CARD_RANKS = ['2', '3', '4', '5', '6', 
              '7', '8', '9', '10', 
              'J', 'Q', 'K', 'A']

def generate_cart():
    return choice(CARD_RANKS), choice(CARD_SUITS)

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()
    one_btn = InlineKeyboardButton('1', callback_data="1")
    two_btn = InlineKeyboardButton('2', callback_data="2")
    three_btn = InlineKeyboardButton('3', callback_data="3")
    # four_btn = InlineKeyboardButton('4', callback_data="4")
    
    keyboard.add(one_btn, two_btn, three_btn)
    bot.reply_to(
        message, 
        "Доброе время суток!\n"
        "Выберите сложность игры от 1 (менее сложный) до 4 (самый сложный):", 
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: call.data in ['1', '2', '3'])
def handle_difficulty_selection(call):
    if call.data == '1':
        keyboard = InlineKeyboardMarkup()
        red_btn = InlineKeyboardButton('🟥', callback_data="R")
        black_btn = InlineKeyboardButton('⬛️', callback_data="B")

        keyboard.add(red_btn, black_btn)
        bot.send_message(
            call.message.chat.id, 
            "Вы выбрали сложность 1 (менее сложный)\n"
            "Вам необходимо угадать цвет карты (черный или красный)", 
            reply_markup=keyboard
        )
    elif call.data == '2':
        keyboard = InlineKeyboardMarkup()
        spades_btn = InlineKeyboardButton('♠️', callback_data="♠️")
        hearts_btn = InlineKeyboardButton('♥️', callback_data="♥️")
        diamonds_btn = InlineKeyboardButton('♦️', callback_data="♦️")
        clubs_btn = InlineKeyboardButton('♣', callback_data="♣")

        keyboard.add(spades_btn, hearts_btn, diamonds_btn, clubs_btn)
        bot.send_message(
            call.message.chat.id, 
            "Вы выбрали сложность 2 (нормальный)\n"
            "Вам необходимо угадать масть карты (♠️, ♥️, ♦️, ♣).", 
            reply_markup=keyboard
        )
    elif call.data == '3':
        keyboard = InlineKeyboardMarkup()
        b2_btn = InlineKeyboardButton('2', callback_data="2")
        b3_btn = InlineKeyboardButton('3', callback_data="3")
        b4_btn = InlineKeyboardButton('4', callback_data="4")
        b5_btn = InlineKeyboardButton('5', callback_data="5")
        b6_btn = InlineKeyboardButton('6', callback_data="6")
        b7_btn = InlineKeyboardButton('7', callback_data="7")
        b8_btn = InlineKeyboardButton('8', callback_data="8")
        b9_btn = InlineKeyboardButton('9', callback_data="9")
        b10_btn = InlineKeyboardButton('10', callback_data="10")
        bJ_btn = InlineKeyboardButton('J', callback_data="J")
        bQ_btn = InlineKeyboardButton('Q', callback_data="Q")
        bK_btn = InlineKeyboardButton('K', callback_data="K")
        bA_btn = InlineKeyboardButton('A', callback_data="A")

        keyboard.add(b2_btn, b3_btn, b4_btn, b5_btn, b6_btn, b7_btn, b8_btn, b9_btn, b10_btn, bJ_btn, bQ_btn, bK_btn, bA_btn)
        bot.send_message(
            call.message.chat.id, 
            "Вы выбрали сложность 3 (сложный)\n"
            "Вам необходимо угадать номинал карты (1-10, J, Q, K или A)", 
            reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: call.data in ['R', 'B'])
def echo_call(call):
    card_rank, card_suit = generate_cart()
    if call.data == "R" and card_suit in ['♦️', '♥️'] \
    or call.data == "B" and card_suit in ['♠️', '♣']:
        bot.send_message(call.message.chat.id, f'Поздравляем! Вы угадали цвет карты! Была загадана карта {card_rank}{card_suit}. Приходите еще!'
        )
    else:
        bot.send_message(call.message.chat.id, f'Вы проиграли! Была загадана карта {card_rank}{card_suit}. Приходите еще! Удачи!'
        )

    start(call.message)
        
@bot.callback_query_handler(func=lambda call: call.data in ["♠️", "♥️", "♦️", "♣"])
def handle_suit_guess(call):
    card_rank, card_suit = generate_cart()
    if call.data == card_suit:
        bot.send_message(call.message.chat.id, f'Поздравляем! Вы угадали масть карты! Была загадана карта {card_rank}{card_suit}. Приходите еще!'
        )
    else:
        bot.send_message(call.message.chat.id, f'Вы проиграли! Была загадана карта {card_rank}{card_suit}. Приходите еще! Удачи!'
        )

    start(call.message)

@bot.callback_query_handler(func=lambda call: call.data in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])
def handle_suit_guess(call):
    card_rank, card_suit = generate_cart()
    if call.data == card_rank:
        bot.send_message(call.message.chat.id, f'Поздравляем! Вы угадали масть карты! Была загадана карта {card_rank}{card_suit}. Приходите еще!'
        )
    else:
        bot.send_message(call.message.chat.id, f'Вы проиграли! Была загадана карта {card_rank}{card_suit}. Приходите еще! Удачи!'
        )

    start(call.message)

bot.infinity_polling()