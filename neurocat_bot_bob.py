# Отправляет обновления боту Telegram. 
# Аргумент **tqdm_kwargs это ключевые аргументы класса tqdm.tqdm().
print("_"*100)
print("Exaple 05 - send to Telegram Bot")
from tqdm.contrib.telegram import trange
from time import sleep

token = '6110210645:AAHIP7f9Pkm2PGtAhoMb2MQeHZXI6mO_q_8'
chat_id = int('251566896')

iterable = 5
for i in trange(iterable, desc='Total', token=token, chat_id=chat_id):
    sleep(3)

import telegram_send
telegram_send.send(messages=["Wow that was easy!"])

"""
from bob_telegram_tools.bot import TelegramBot

print("\nАвторизация бота...")
bot = TelegramBot(token, chat_id)
print("...вроде бы, авторизовались.")


print("\nОтправка в бот сообщения...\n")
sent_message = bot.send_text('Hello TelegramBot!')
bot.update_text(sent_message,'Updated hello TelegramBot!')
"""