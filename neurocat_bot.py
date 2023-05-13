# Отправляет обновления боту Telegram. 
# Аргумент **tqdm_kwargs это ключевые аргументы класса tqdm.tqdm().
print("_"*100)
print("Exaple 05 - send to Telegram Bot")
from tqdm.contrib.telegram import trange
from time import sleep
# import telegram_send


token = '6110210645:AAHIP7f9Pkm2PGtAhoMb2MQeHZXI6mO_q_8'
chat_id = int('251566896')
    
iterable = 10
for i in trange(iterable,ascii=False, token=token, chat_id=chat_id):
    # Описание будет отображаться слева
    i.set_description('GEN %i' %i)
    sleep(1)
    """
    if i % 100 == 0:
        message = f"Completed {i}/{iterable}"
        try:
            telegram_send.send(messages=["Process finished!"])
        except Exception as e:
            print("Unable to send", e)
            """
    

