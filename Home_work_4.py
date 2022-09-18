import functools

user_name = input("Введите ваш логин: ")
admin_account = "400$"
def decorator (account_balance):
    def wrapper_decorator(*args):
        if user_name == "admin":
            return account_balance()
        return print("Доступ запрещён")
    return wrapper_decorator
@decorator
def account_balance ():
    print (f"Остаток на счете : {admin_account}")
account_balance()