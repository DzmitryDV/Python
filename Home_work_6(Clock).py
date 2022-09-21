import datetime
from os import system
import time

s = "\033[" +"101" + "m " + "\033[0m"

# Цифра ноль
def zero(temp: list):
    temp[0] += s * 10 + "  "
    temp[1] += s * 2 + "      " + s * 2 + "  "
    temp[2] += s * 2 + "      " + s * 2 + "  "
    temp[3] += s * 2 + "      " + s * 2 + "  "
    temp[4] += s * 2 + "      " + s * 2 + "  "
    temp[5] += s * 2 + "      " + s * 2 + "  "
    temp[6] += s * 10 + "  "
    return temp

# Цифра один
def one(temp_1: list):
    temp_1[0] += s * 6 + "      "
    temp_1[1] += "    " + s * 2 + "      "
    temp_1[2] += "    " + s * 2 + "      "
    temp_1[3] += "    " + s * 2 + "      "
    temp_1[4] += "    " + s * 2 + "      "
    temp_1[5] += "    " + s * 2 + "      "
    temp_1[6] += s * 9 +"   "
    return temp_1

# Цифра два
def two(temp_2: list):
    temp_2[0] += s * 10 + "  "
    temp_2[1] += "        " + s * 2 + "  "
    temp_2[2] += "        " + s * 2 + "  "
    temp_2[3] += s * 10 + "  "
    temp_2[4] += s * 2 + "          "
    temp_2[5] += s * 2 + "        "  + "  "
    temp_2[6] += s * 10 + "  "
    return temp_2

# Цифра три
def three(temp_3: list):
    temp_3[0] += s * 10 + "  "
    temp_3[1] += "        " + s * 2 + "  "
    temp_3[2] += "        " + s * 2 + "  "
    temp_3[3] += s * 10 + "  "
    temp_3[4] += "        " + s * 2 + "  "
    temp_3[5] += "        " + s * 2 + "  "
    temp_3[6] += s * 10 + "  "
    return temp_3

# Цифра четыре
def four(temp_4: list):
    temp_4[0] += s * 2 + "      " + s * 2 + "  "
    temp_4[1] += s * 2 + "      " + s * 2 + "  "
    temp_4[2] += s * 2 + "      " + s * 2 +  "  "
    temp_4[3] += s * 10 + "  "
    temp_4[4] += "        " + s * 2 + "  "
    temp_4[5] += "        " + s * 2 + "  "
    temp_4[6] += "        " + s * 2 + "  "
    return temp_4

# Цифра пять
def five(temp_5: list):
    temp_5[0] += s * 10 + "  "
    temp_5[1] += s * 2 + "        " + "  "
    temp_5[2] += s * 2 + "        " + "  "
    temp_5[3] += s * 10 + "  "
    temp_5[4] += "        " + s * 2 + "  "
    temp_5[5] += "        " + s * 2 + "  "
    temp_5[6] += s * 10 + "  "
    return temp_5

# Цифра шесть
def six(temp_6: list):
    temp_6[0] += s * 10 + "  "
    temp_6[1] += s * 2 + "        " + "  "
    temp_6[2] += s * 2 + "        " + "  "
    temp_6[3] += s * 10 + "  "
    temp_6[4] += s * 2 +"      " + s * 2 + "  "
    temp_6[5] += s * 2 + "      " + s * 2 + "  "
    temp_6[6] += s * 10 + "  "
    return temp_6

# Цифра семь
def seven(temp_7: list):
    temp_7[0] += s * 10 + "  "
    temp_7[1] += "        " + s * 2 + "  "
    temp_7[2] += "        " + s * 2 + "  "
    temp_7[3] += "        " + s * 2 + "  "
    temp_7[4] += "        " + s * 2 + "  "
    temp_7[5] += "        " + s * 2 + "  "
    temp_7[6] += "        " + s * 2 + "  "
    return temp_7

# Цифра восемь
def eight(temp_8: list):
    temp_8[0] += s * 10 + "  "
    temp_8[1] += s * 2 + "      " + s * 2 + "  "
    temp_8[2] += s * 2 + "      " + s * 2 + "  "
    temp_8[3] += s * 10 + "  "
    temp_8[4] += s * 2 + "      " + s * 2 + "  "
    temp_8[5] += s * 2 + "      " + s * 2 + "  "
    temp_8[6] += s * 10 + "  "
    return temp_8

# Цифра девять
def nine(temp_9: list):
    temp_9[0] += s * 10 + "  "
    temp_9[1] += s * 2 + "      " + s * 2 + "  "
    temp_9[2] += s * 2 + "      " + s * 2 + "  "
    temp_9[3] += s * 10 + "  "
    temp_9[4] += "        " + s * 2 + "  "
    temp_9[5] += "        " + s * 2 + "  "
    temp_9[6] += s * 10 + "  "
    return temp_9

# Сепаратор
def sep_1(value: list):
    value[0] += "     "
    value[1] += " " + s * 2 + "  "
    value[2] += " " + s * 2 + "  "
    value[3] += "     "
    value[4] += " " + s * 2 + "  "
    value[5] += " " + s * 2 + "  "
    value[6] += "     "
    return value

# без сепаратора
def sep_2(value: list):
    value[0] += "     "
    value[1] += "   " + "  "
    value[2] += "   " + "  "
    value[3] += "     "
    value[4] += "   " + "  "
    value[5] += "   " + "  "
    value[6] += "     "
    return value

# Изменение цветовой схемы
def clock_color(q: str, i: int):
    if i >= 0 and i <= 9:
        q = q.replace("101", "102")
    elif i >= 10 and i <= 19:
        q = q.replace("102", "103")
    elif i >= 20 and i <= 29:
        q = q.replace("103", "104")
    elif i >= 30 and i <= 39:
        q = q.replace("104", "105")
    elif i >= 40 and i <= 49:
        q = q.replace("105", "106")
    elif i >= 50 and i <= 59:
        q = q.replace("106", "107")
    elif i >= 60 and i <= 69:
        q = q.replace("107", "101")
        if i == 69:
            i = 0
    return q, i
counter_1 = 0 # Счетчик для сепаратора
counter_2 = 0 # Счетчик для изменения цвета

# Цикл для часов
while True:
    counter_2 +=  1
    s, counter_2 = clock_color(s, counter_2)
    lines = ["", "", "", "", "", "", ""]
    system("clear")
    clock = datetime.datetime.now()
    clock = clock.strftime("%H%M%S") # Приводим к сторовому типу >> "141552"
    clock = list(clock)             # Приводим к типу список >> ["1", "4", "1", "5", "5", "2"]
    clock = [int(i) for i in clock] # Преобразуем строковые элементы в инт >> [141552]

    for i in clock:            # Проходимся циклом по списку, достаём цифру и закидываем в нужную функцию 
        counter_1 = counter_1 + 1
        if i == 0:
            digit = zero(lines)
        if i == 1:
            digit = one(lines)
        if i == 2:
            digit = two(lines)
        if i == 3:
            digit = three(lines)
        if i == 4:
            digit = four(lines)
        if i == 5:
            digit = five(lines)
        if i == 6:
            digit = six(lines)
        if i == 7:
            digit = seven(lines)
        if i == 8:
            digit = eight(lines)
        if i == 9:
            digit = nine(lines)
        if counter_1 == 2:                 # Здесь логика для сепаратора
            digit = sep_1(digit)           
        if counter_1 == 4:                 
            digit = sep_1(digit)           
        if counter_1 == 8:                 
            digit = sep_2(digit)           
        if counter_1 == 10:                
            digit = sep_2(digit)          
            counter_1 = -2                 
        new_watch = "\n".join(digit)       # Здесь преобразуем список в строку

    print(new_watch)   
    time.sleep(0.3)