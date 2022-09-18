from os import system
import math
x = 0
y = 0
user_command = [0, 0]
print("Вы находитесь в программе робота - дальнобойщика \nЧтобы отправиться в путь, следуйте инструкциям ниже: ")

# Функция меню
def menu (value):
    print("\n1. Ход вверх, введите u")
    print("2. Ход вниз, введите d")
    print("3. Ход вправо, введите r")
    print("4. Ход влево, введите l")
    print("5. Завершить ходы, введите пробел")
    value = input("\nВведите команду, а через пробел количество километров: ").split()
    return value

while len(user_command) != 0:          # Пока наш список не пустой, то выполняем цикл
    user_command.clear                 # Чистим список
    user_command = menu(user_command)  # Запускаем меню и просим ввести команду для робота

    # Здесь обрабатывается ошибка, если второй позицией будет не цифра
    while len(user_command) > 1 and user_command[1] != int: 
        try:
            user_command[1] = int(user_command[1])
            break            
        except:
            system('cls')
            print("Ошибка ввода!\n")
            user_command = menu(user_command)

    # Здесь логика по перемещению робота
    if len(user_command) > 1 and len(user_command) < 3 and  user_command[0] == "u":   # Если идём вверх, то прибавляем количество шагов
        y = y + int(user_command[1])                        
    elif len(user_command) > 1 and len(user_command) < 3 and  user_command[0] == "d": # Если идём вниз, то вычитаем количество шагов
        y = y - int(user_command[1])
    elif len(user_command) > 1 and len(user_command) < 3 and  user_command[0] == "r": # Если идём вправо, то прибавляем количество шагов
        x = x + int(user_command[1])
    elif len(user_command) > 1 and len(user_command) < 3 and  user_command[0] == "l": # Если идём влево, то вычитаем количество шагов
        x = x - int(user_command[1])
    elif len(user_command) != 0:   # Логика на ошибку ввода
        system('cls')
        print("Ошибка ввода!\n")
system('cls')
robot_distance = math.sqrt((x ** 2) + (y ** 2)) # Формула расчета пройденного растояния
robot_distance = round(robot_distance, 2)       # Округляем до 2 знаков после запятой
print(f"Вы завершили программу. \n\nРобот - дальнобойщик находится в пункте разгрузки с координатами: x{x}, y{y}")
print(f"Пройденное расстояние: {robot_distance} км \n\n")