import random
import requests
import telebot
from config import token
bot = telebot.TeleBot(token)
import os
print(os.listdir('consciques_ofpollution'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")


@bot.message_handler(commands=['paper'])
def send_bye(message):
    bot.reply_to(message, "Сроки разложения бумаги зависят от её вида: 1 Газетная бумага разлагается от 1 до 4 месяцев. Срок зависит от количества краски на бумаге и толщины листов. 1Картонные коробки или картон имеют период разложения от 3 до 6 месяцев. 1 Офисная бумага разлагается примерно 2 года.")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['glass'])
def send_bye(message):
    bot.reply_to(message, "Стекло практически не разлагается. 1 По оценкам некоторых исследований, для разрушения стекла требуется около миллиона лет.")

@bot.message_handler(commands=['plastic'])
def send_bye(message):
    bot.reply_to(message, "Срок разложения пластика зависит от его типа. Например, пластиковые бутылки могут разлагаться более 450 лет, а пластиковые пакеты — более 100 лет. 1Некоторые примерные сроки разложения разных видов пластика:PET (полиэтилентерефталат) — от 450 до 500 лет; 2HDPE (полиэтилен высокой плотности) — от 100 до 500 лет; 2PVC (поливинилхлорид) — более 500 лет; 2LDPE (полиэтилен низкой плотности) — от 100 до 500 лет; 2PP (пропилен) — от 100 до 500 лет; 2PS (полистирол) — от 500 до 700 лет. 2Некоторые виды пластика, такие как пенополистирол, не разлагаются вовсе. 1Для разложения полимеров необходимо сочетание определённой температуры, влажности, наличие кислорода и специфических микроорганизмов. В естественной среде, особенно на свалках, такие условия редко создаются.")


@bot.message_handler(commands=['eco_activist'])
def send_bye(message):
    bot.reply_to(message, "Разложение материалов происходит в результате различных химических реакций. Из одного, более сложного вещества образуются два или более других, более простых веществ. 1Некоторые виды разложения:Биодеградация. 12 Разложение в результате деятельности живых организмов. 1Сольволиз. Реакция обменного разложения между растворённым веществом и растворителем. 1Радиолиз. Разложение под действием ионизирующих излучений.")

@bot.message_handler(commands=['consciques'])
def send_mems(message):
    forest = random.choice(os.listdir('consciques_ofpollution'))
    with open(f'consciques_ofpollution/{forest}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open('images/mem1.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

def get_duck_image_url():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.message_handler(commands=['dog'])
def duck(message):
    '''По команде dog вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)



bot.polling()
