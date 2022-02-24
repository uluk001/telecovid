import telebot
import requests
import json
import datetime
token='5208355387:AAFKIE9J2EvVXv7a-jVhMCfXFya5OnGO90A'
bot = telebot.TeleBot(token=token)
covid_api = 'https://covid-api.mmediagroup.fr/v1/cases?country={country}'

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, "Привет, Я Covid19-бот напишите страну")

@bot.message_handler(content_types='text')
def send_data(message):
    covid = requests.get(covid_api.format(country=message.text.title()))
    covid_json = covid.json()
    con = covid_json['All']['confirmed']
    de = covid_json['All']['deaths']
    re = covid_json['All']['recovered']
    co = covid_json['All']['country']
    po = covid_json['All']['population']
    bot.send_message(message.chat.id, f'🤒 Подтвержденный { con }')
    bot.send_message(message.chat.id, f'💀 Умерших { de }')
    bot.send_message(message.chat.id, f'😷 Выздоровел { re }')
    bot.send_message(message.chat.id, f'страна :{ co }')
    bot.send_message(message.chat.id,f'Население : { po }')
    today = datetime.datetime.now()
    data = f'Количество заболевших коронавирусом в г. {message.text.title()}: {covid_json["All"]["confirmed"]} дата сегодня: {today.day}-{today.month}-{today.year}'
    bot.send_message(message.chat.id, data)

print('Бот работает.....')
bot.infinity_polling()