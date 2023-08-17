import telebot
import requests
import random
from bs4 import BeautifulSoup

token = '5740098401:AAGVDcr0A2JLskF0dEvuH8puX_c5AS4p5dE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!
    """
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворение..."
    bot.send_message(message.chat.id, poem_text)

@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['random_game'])
def send_advice(message):
    vibor_janra = '''Привет! Я умею предлагать игры по выбранному жанру! У меня есть 6 жанров:
    1. Adventure
    2. Puzzle
    3. Fantasy
    4. Online
    5. Shooter
    6. Open-World'''
    bot.send_message(message.chat.id, vibor_janra)

@bot.message_handler(func=lambda message: True)
def poluchenie_igri(message):
    if message.text == "Adventure" or message.text == '1':
        bot.send_message(message.from_user.id, "Doom")
        bot.send_message(message.from_user.id, "Steam link: [Doom](https://store.steampowered.com/app/379720/Doom/)")
    elif message.text == "Puzzle" or message.text == '2':
        bot.send_message(message.from_user.id, "Portal 2")
        bot.send_message(message.from_user.id, "Steam link: [Portal 2](https://store.steampowered.com/app/620/Portal_2/)")
    elif message.text == "Fantasy" or message.text == '3':
        bot.send_message(message.from_user.id, "Starfield")
        bot.send_message(message.from_user.id, "Steam link: [Starfield](https://store.steampowered.com/app/123456/Starfield/)")
    elif message.text == "Online" or message.text == '4':
        bot.send_message(message.from_user.id, "Dota 2")
        bot.send_message(message.from_user.id, "Steam link: [Dota 2](https://store.steampowered.com/app/570/Dota_2/)")
    elif message.text == "Shooter" or message.text == '5':
        bot.send_message(message.from_user.id, "CoD")
        bot.send_message(message.from_user.id, "Steam link: [Call of Duty](https://store.steampowered.com/app/12345/Call_of_Duty/)")
    elif message.text == "Open-World" or message.text == '6':
        bot.send_message(message.from_user.id, "Cyberpunk 2077")
        bot.send_message(message.from_user.id, "Steam link: [Cyberpunk 2077](https://store.steampowered.com/app/1091500/Cyberpunk_2077/)")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши жанр как в описании команды или отправь цифру жанра.")

bot.polling()


