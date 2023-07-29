# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


balance = 0
put_counter = 0
take_counter = 0
MULTYPLICITY = 50
TAKE_PERCENT = 1.5
MIN_PERCENT = 30
MAX_PERCENT = 600
THIRD_OPER_PERCENT = 3
TAX_PERCENT = 10
MAX_BALANCE = 5000000
list_all_money = []


# положить деньги
def putMoney(money: int, list_money: list) -> int:
    global balance
    balance += money
    list_money.append(money)
    return balance


# снять деньги
def takeMoney(money: int, list_money: list) -> int:
    global balance
    balance -= money
    list_money.append(-money)
    return balance


# получаем деньги и чекаем на кратность 50
def checkMult(message: str) -> int | str:
    global balance
    while True:
        try:
            money = int(input(message))
            if money > 0 and money % MULTYPLICITY == 0:
                return money
            else:
                print("Сумма пополнения и снятия должна быть больше 0 и кратна 50, попробуйте ещё раз")
                print(f"Баланс карты: {balance} у.е")
                print(f"История всех операций: {list_all_money}")
                print()
        except ValueError:
            print("Ввод некорректен")


# начисление процента от суммы снятия 1.5%
def procMoney(money: int) -> int:
    prMoney = money / 100 * TAKE_PERCENT
    if prMoney < MIN_PERCENT:
        money += MIN_PERCENT
    elif prMoney > MAX_PERCENT:
        money += MAX_PERCENT
    else:
        money += prMoney
        print(money)
    return money


# начисление процента после каждой 3-ей операции
def thirdOper(list_money: list) -> None:
    global balance
    prMoney = balance / 100 * THIRD_OPER_PERCENT
    putMoney(prMoney, list_money)


# налог на роскошь
def luxury_tax(list_money: list) -> None:
    global balance
    if balance > MAX_BALANCE:
        prMoney = balance / 100 * TAX_PERCENT
        takeMoney(prMoney, list_money)


# функция подсчёта
def work():
    global balance, put_counter, take_counter, list_all_money
    print("Доброе пожаловать в приложение банкомат!")
    while True:
        action = int(input("Выберите команду:\n"
                       "1 – пополнить баланс\n"
                       "2 – снять деньги\n"
                       "3 – выйти\n"))
        luxury_tax(list_all_money)
        match action:
            case 1:
                pMoney = checkMult("Введите сумму пополнения: ")
                putMoney(pMoney, list_all_money)
                put_counter += 1
                if put_counter == 3:
                    thirdOper(list_all_money)
                    put_counter = 0
                print(f"Баланс карты: {balance} у.е")
                print(f"История всех операций: {list_all_money}")
                print()
            case 2:
                tMoney = checkMult("Введите сумму снятия: ")
                tMoney = procMoney(tMoney)
                if tMoney <= balance:
                    takeMoney(tMoney, list_all_money)
                    take_counter += 1
                    if take_counter == 3:
                        thirdOper(list_all_money)
                        take_counter = 0
                else:
                    print("На карте недостаточно денег для снятия")
                print(f"Баланс карты: {balance} у.е")
                print(f"История всех операций: {list_all_money}")
                print()
            case 3:
                print("Всего хорошего, до свидания!")
                print(f"Баланс карты: {balance} у.е")
                print(f"История всех операций: {list_all_money}")
                print()
                break
            case _:
                print("Что-то пошло нет так, введите цифру от 1 до 3")

# старт
work()


