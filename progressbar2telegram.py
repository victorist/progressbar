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

nepoch = 1
iterable = 10
tlossvalue = 0.871
taccuracy = 0,777
with trange(iterable, ascii=False, token=token, chat_id=chat_id) as t:
    for i in t:
        # Описание будет отображаться слева
        t.set_description('Epoch %i' %nepoch)
        # postfix будет отображаться справа,
        # форматируется автоматически на основе типа данных аргумента
        t.set_postfix(TL=tlossvalue, TA=taccuracy)
        sleep(0.5)

"""
with tqdm(total=10, bar_format="{postfix[0]} {postfix[1][value]:>8.2g}",
          postfix=["Batch", dict(value=0)]) as t:
    for i in range(10):
        sleep(0.5)
        t.postfix[1]["value"] = i / 2
        t.update()
"""


"""   
iterable = 10
for i in trange(iterable,ascii=False, token=token, chat_id=chat_id):
    # Описание будет отображаться слева
    #i.set_description('GEN %i' % i)
    sleep(1)
"""