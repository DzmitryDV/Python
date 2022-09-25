import datetime
from os import system
import time
from functools import partial

s = "\033[" +"101" + "m " + "\033[0m"
x = " "
new_dict = {
    "0": [s * 10 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 10 + x * 2],
    "1": [s * 6 + x * 6, x * 4 + s * 2 + x * 6, x * 4 + s * 2 + x * 6, x * 4 + s * 2 + x * 6, x * 4 + s * 2 + x * 6, x * 4 + s * 2 + x * 6, s * 9 + x * 3],
    "2": [s * 10 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2, s * 10 + x * 2, s * 2 + x * 10, s * 2 + x * 10, s * 10 + x * 2],
    "3": [s * 10 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2, s * 10 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2, s * 10 + x * 2],
    "4": [s * 2 + x * 6 + s * 2 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 10 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2],
    "5": [s * 10 + x * 2, s * 2 + x * 8 + x * 2, s * 2 + x * 8 + x * 2, s * 10 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2, s * 10 + x * 2],
    "6": [s * 10 + x * 2, s * 2 + x * 10, s * 2 + x * 10, s * 10 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 10 + x * 2],
    "7": [s * 10 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2],
    "8": [s * 10 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 10 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 10 + x * 2],
    "9": [s * 10 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 2 + x * 6 + s * 2 + x * 2, s * 10 + x * 2, x * 8 + s * 2 + x * 2, x * 8 + s * 2 + x * 2, s * 10 + x * 2],
    ":": [x * 5, x + s * 2 + x * 2, x + s * 2 + x * 2, x * 5, x + s * 2 + x * 2, x + s * 2 + x * 2, x * 5],
    "w:": [x * 5, x * 5, x * 5, x * 5, x * 5, x * 5, x * 5]
}

# Плюсуем строки
def new_clock(a: list, b: list ):
    a[0] += b[0]
    a[1] += b[1]
    a[2] += b[2]
    a[3] += b[3]
    a[4] += b[4]
    a[5] += b[5]
    a[6] += b[6]
    return a
   
# Изменение цветовой схемы
def clock_color(q: str,i: int):
    if i > 10 and i < 21:
        q = q.replace("101", "102")
    if i > 20 and i < 31:
        q = q.replace("101", "103")
    if i > 30 and i < 41:
        q = q.replace("101", "104")
    if i > 40 and i < 51:
        q = q.replace("101", "105") 
    if i > 50 and i < 61:
        q = q.replace("101", "106") 
    if i > 60 and i < 71:
        q = q.replace("101", "107") 
        if i == 70:
            i = 0
    return q, i
    
counter_1 = 0 # Счетчик для сепаратора
counter_2 = 0 # Счетчик для изменения цвета

# Цикл для часов
while True:
    system("clear")
    counter_2 +=  1
    digit = ["", "", "", "", "", "", ""]
    clock = datetime.datetime.now().strftime("%H%M%S") # Получаем время и приводим к сторовому типу >> "141552"
    for i in clock: 
        lines = new_dict.get(i)           
        counter_1 += 1
        digit = new_clock(digit, lines)
        if counter_1 == 2:                          # Здесь логика для сепаратора
            digit = new_clock(digit, new_dict[":"])           
        if counter_1 == 4:                 
            digit = new_clock(digit, new_dict[":"])           
        if counter_1 == 8:                 
            digit = new_clock(digit, new_dict["w:"])           
        if counter_1 == 10:                
            digit = new_clock(digit, new_dict["w:"])          
            counter_1 = -2                 
        new_watch = "\n".join(digit)                 # Здесь преобразуем список в строку
    new_watch, counter_2 = clock_color(new_watch, counter_2)
    print(new_watch)   
    time.sleep(0.3)
