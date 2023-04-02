
# Exemple 01
print("_"*100)
print("Exaple 01")
from tqdm import tqdm
from time import sleep
# оборачиваем итератор range(100) классом tqdm()
for i in tqdm(range(20), ncols=80, ascii=True, desc='Total'):
    sleep(0.1)

# Example 02
print("_"*100)
print("Exaple 02")
text = ""
for char in tqdm(["a", "b", "c", "d"], ncols=80):
    sleep(0.1)
    text = text + char
    tqdm.write(text)

# Example 03
# Класс tqdm.trange(i) - это специальный оптимизированный экземпляр tqdm.tqdm(range(i)). 
# Аргументы, которые он принимает при инициализации, 
# аналогичны конструктора класса tqdm.tqdm():
print("_"*100)
print("Exaple 03")
from tqdm import trange
from time import sleep
for i in trange(20, ncols=80, desc='Total'):
     sleep(0.1)

# Exemple 04
# Создание экземпляра tqdm.tqdm() вне цикла позволяет вручную управлять
#  строкой progressbar и добавлять динамические/обновляемые данные:
print("_"*100)
print("Exaple 04")
from tqdm import tqdm
from time import sleep
pbar = tqdm(["a", "b", "c", "d"], ncols=80)
for char in pbar:
     sleep(1)
     # добавление префикса и элементов итерации к прогресс бару

# Exemple 05
# Модуль tqdm поддерживает вложенные индикаторы выполнения. Смотрим пример:
print("_"*100)
print("Exaple 05")
from tqdm.auto import trange
from time import sleep
for i in trange(4, desc='loop-1'):
    for j in trange(5, desc='loop-2'):
        for k in trange(50, desc='loop-3', leave=False):
            sleep(0.01)

# Exemple 05
# Ручное управление обновлениями строки прогресс бара класса tqdm() с 
# помощью оператора with (могут быть проблемы с обновлением):
print("_"*100)
print("Exaple 06")
from time import sleep
from tqdm import tqdm
with tqdm(total=30) as pbar:
    for i in range(3):
        sleep(0.1)
        pbar.update(10)


# Example 06
# Отправляет обновления боту Telegram. 
# Аргумент **tqdm_kwargs это ключевые аргументы класса tqdm.tqdm().
print("_"*100)
print("Exaple 07 - send to Telegram Bot")
from tqdm.contrib.telegram import tqdm, trange
from time import sleep

iterable = 5
for i in trange(iterable, ncols=40, desc='Total', token='6110210645:AAHIP7f9Pkm2PGtAhoMb2MQeHZXI6mO_q_8', chat_id='251566896'):
    sleep(2)

# Example 07
# Writing messages
print("_"*100)
print("Exaple 08 - Writing messages")
from tqdm.auto import tqdm, trange
from time import sleep

bar = trange(10)
for i in bar:
    # Print using tqdm class method .write()
    sleep(0.1)
    if not (i % 3):
        tqdm.write("Done task %i" % i)
    # Can also use bar.write()