a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье число "))

# Шаг 1:
result_1 = a and b and c and print (" \n ШАГ1 \n Нет нулевых значений")

# Шаг 2:
print ("\n ШАГ 2")
temp_1 = a or b or c or "Вы ввели все нули"
print("Первое НЕнулевое значение: ", temp_1)

# Шаг 3:  
if a > b + c:
    result_2 = a - b - c
    print ("\n Шаг 3 \n Первое число больше чем сумма второго и третьего чисел, результат a - b - c: ", result_2)

# Шаг 4:
if a < b + c:
    result_3 = b + c - a
    print ("\n Шаг 4 \n Первое число меньше чем сумма второго и третьего чисел, результат b + c - a: ", result_3)

# Шаг 5:
if a > 50 and (b > a or c > a):
    print("\n Шаг 5 \n Вася")

# Шаг 6:
if a > 5 or (b == 7 and c == 7):
    print("\n Шаг 6 \n Петя")