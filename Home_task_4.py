import functools
from math import degrees
user_name = input("Введите ваш логин: ")
admin_account = "400$"
def decorator (account_balance):
    def wrapper_decorator(*args):
        if user_name != "admin":
            return print("Доступ запрещён")
        account_balance()
    return wrapper_decorator
@decorator
def account_balance ():
    print (f"Остаток на счете : {admin_account}")
account_balance()