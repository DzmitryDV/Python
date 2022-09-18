import functools
from os import system

users_dict = {"Вася": 
                    {"Рост": 1.74, 
                    "Вес": 68, 
                    "Пол": "М", 
                    "BMI": 22.46, 
                    "Шкала BMI": "16======|============================50"}, 
             "Петя": 
                    {"Рост": 1.85, 
                    "Вес": 82, 
                    "Пол": "М", 
                    "BMI": 23.96, 
                    "Шкала BMI": "16=======|===========================50"}
}

# Функция высчитывающая BMI
def bmi_user_result(weight, growth):
        value = weight / (growth * growth)
        value = round(value, 2)
        return value

# Функция делает шкалу BMI
def bmi_scale(a):
        rezult_1 = a - 16                   
        rezult_1 = int(rezult_1)            
        rezult_2 = 34 - rezult_1
        if a < 18.5:
            return  "16" + "=" * rezult_1 + "|" + "=" * rezult_2 + "50"
        elif 18.5 < a < 25:
            return  "16" + "=" * rezult_1 + "|" + "=" * rezult_2 + "50"
        elif 25 < a < 30:
             return "16" + "=" * rezult_1 + "|" + "=" * rezult_2 + "50"
        elif 30 < a < 35:
             return "16" + "=" * rezult_1 + "|" + "=" * rezult_2 + "50"
        elif 35 < a < 40:
             return "16" + "=" * rezult_1 + "|" + "=" * rezult_2 + "50"
        elif a > 40:
             return "16" + "=" * rezult_1 + "|" + "=" * rezult_2 + "50"

# Функция Меню
def main_menu():
    def menu():
        system('cls')
        print ("\n       Главное Меню:")
        print ("\n1. Посмотреть список пользователей")
        print ("2. Посмотреть информацию о пользователе")
        print ("3. Изменить информацию о пользователе")
        print ("4. Удалить пользователя")
        print ("5. Добавить пользователя")
        print ("6. Выйти")
        value_1 = input("\nВведите пункт меню: ")
        return value_1
    value_2 = menu()

    # Функция на проверку ввода числа
    def test_parametr (a):
        while a != int:
            try:
                a = int(a)
                break
            except:
                system('cls')
                print("Ошибка ввода! Нужно вводить число\n")
                input("Нажмите Ввод для продолжения")
                a = menu()
        return a
    value_2 = test_parametr(value_2)
    while value_2 < 1 or value_2 > 6:
        system('cls')
        print("Ошибка ввода! Нет такого пункта меню\n")
        input("Нажмите Ввод для продолжения")
        value_2 = menu()
        value_2 = test_parametr(value_2)
    return value_2

# Функция добавления нового пользователя
def new_user():
    system('cls')
    user_name = input("Введите имя пользователя: ")
    user_growth = float(input("Введите рост пользователя, м: "))
    user_weight = float(input("Введите вес пользователя, кг: "))
    user_gender = int(input("Введите 1, если это мужчина \nВведите 2 если это женщина: "))

    # Декоратор
    def decorator (gender_request):
        def wrapper_decorator(*args):
            while user_gender < 1 or user_gender > 2:
                print ("\n Вы ввели не верное значение! \n")
                value = int(input("Введите 1, если это мужчина \nВведите 2 если это женщина: "))
                if value == 1:
                    value = "М"
                    return value
                if value == 2:
                    value = "Ж"
                    return value
            return gender_request(user_gender)
        return wrapper_decorator

    # Декорированная функция на определение пола пользователя    
    @decorator
    def gender_request(temp):
        if temp == 1:
            temp = "М"
            return temp
        if temp == 2:
            temp = "Ж"
            return temp

    user_gender = gender_request(user_gender)
    user_bmi = bmi_user_result(user_weight, user_growth)
    user_bmi_scale = bmi_scale(user_bmi)
    users_dict[user_name] = {"Рост": user_growth, "Вес": user_weight, "Пол": user_gender, "BMI": user_bmi, "Шкала BMI": user_bmi_scale}
    system('cls')
    print(f"\nДобавленный пользователь {user_name}: ")
    for k, v in users_dict[user_name].items():
            print (f"{k}: {v}")

# Функция вывода списка пользователей
def show_users_list():
    system('cls')
    print("\nСписок пользователей: \n")
    for login in users_dict:
        print (login)

# Функция вывода информации о пользователе
def show_user_information():
    def user_information():
        system('cls')
        print("\n\nВыберите пользователя из списка: \n")
        for login in users_dict.keys():
            print (f"Логин: {login}")
        value = input("\nВведите имя здесь: ")
        return value
    user_choice = user_information()
    if user_choice not in users_dict:
        x = False
        while x == False:
            system('cls')
            print(f"\n\nПользователя {user_choice} нет в базе")
            input("\n\nНажмите Ввод для продолжжения")
            user_choice = user_information()
            x = user_choice in users_dict
    if user_choice in users_dict.keys():
        system('cls')
        print(f"\nИнформация о пользователе {user_choice}: ")
        for k, v in users_dict[user_choice].items():
            print (f"{k}: {v}")
    

# Функция изменения информации о пользователе
def edit_user_information ():
    system('cls')
    print("\nСписок пользователей в базе данных: ")
    for login in users_dict:
        print (login)
    user_choice_1= input("\nВведите имя пользователя: ")
    system('cls')
    print ("\nВведите данные, которые хотите изменить: \t")
    for k in users_dict[user_choice_1]:
        print (k)
    user_choice_2 = input("\nВведите параметр здесь: ")
    system('cls')
    if user_choice_2 in users_dict[user_choice_1]:
        new_value = float(input(f"\nВведите новое значение параметра {user_choice_2}: "))
        system('cls')
        users_dict[user_choice_1][user_choice_2] = new_value
        if user_choice_2 =="Рост" or user_choice_2 == "Вес":
            users_dict[user_choice_1]["BMI"] = bmi_user_result(users_dict[user_choice_1]["Вес"], users_dict[user_choice_1]["Рост"])
            users_dict[user_choice_1]["Шкала BMI"] = bmi_scale(users_dict[user_choice_1]["BMI"])
    print (f"\nДанные пользователя {user_choice_1} успешно изменены: ")
    for k, v in users_dict[user_choice_1].items():
        print (f"{k}: {v}")

# Функция удаляет пользователя
def del_user ():
    system('cls')
    print("\nСписок пользователей в базе данных: ")
    for login in users_dict:
        print (login)
    user_choice = input("\nВведите имя пользователя, которого хотите удалить: ")
    if user_choice in users_dict:
        del users_dict[user_choice]
        system('cls')
        print(f"Пользователь {user_choice} успешно удален")
    else:
        system('cls')
        print(f"Пользователя {user_choice} нет в базе")

# Функция "Продолжить" или "Завершить"
def exit_or_continue ():
    request = input("\nВернуться в главное меню? y/n:  ")
    if request == "y":
            step_main_menu(main_menu())
    elif request == "n":
        system('cls')
        print("Программа завершена")
    else:
        system('cls')
        print("Вы ввели не верную команду! \n")
        input("Нажмите Ввод для выхода в глвное меню")
        step_main_menu(main_menu())

# Функция выбора действия в главном меню           
def step_main_menu(my_choice):
    if my_choice == 1:
        show_users_list()
        exit_or_continue()
    elif my_choice == 2:
        show_user_information()
        exit_or_continue()
    elif my_choice == 3:
        edit_user_information()
        exit_or_continue()
    elif my_choice == 4:
        del_user()
        exit_or_continue()
    elif my_choice == 5:
        new_user()
        exit_or_continue()
    elif my_choice == 6:
        system('cls')
        print("\nПрограмма завершена\n\n")  
    

step_main_menu(main_menu())
