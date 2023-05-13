# Отправляет обновления боту Telegram. 
# Аргумент **tqdm_kwargs это ключевые аргументы класса tqdm.tqdm().
token = '6110210645:AAHIP7f9Pkm2PGtAhoMb2MQeHZXI6mO_q_8'
chat_id = int('251566896')

print("_"*100)
print("Exaple 05 - send to Telegram Bot")
#from tqdm import tqdm, trange
from tqdm.contrib.telegram import trange
from random import random, randint
from time import sleep

# conda install -c conda-forge telegram-send
# import telegram_send


nepoch = 1
iterable = 3
tlossvalue = 0.871
taccuracy = 0.777

# telegram_send.send(messages=["Process finished!"])

with trange(iterable, ascii=False, token=token, chat_id=chat_id) as t:
    for i in t:
        # Описание будет отображаться слева
        t.set_description('Epoch %i' %i)
        # postfix будет отображаться справа,
        # форматируется автоматически на основе типа данных аргумента
        t.set_postfix(TL=tlossvalue, TA=taccuracy)

        nround = 1
        iterable2 = 4

        with trange(iterable2, ascii=" .U", token=token, chat_id=chat_id) as t2:
            for i in t2:
                t2.set_description('Round %i' %i)
                # t2.set_postfix(TL=tlossvalue, TA=taccuracy)
                sleep(2.0)

'''
for i in trange(3, desc='1st loop'):
    for j in tqdm(range(100), desc='2nd loop'):
        sleep(0.01)
'''
