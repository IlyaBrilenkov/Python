# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

import re

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money >= 0:
        person['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    if choice == 1:
        print(check_account(person))
    elif choice == 2:
        count = float(input('Сумма к снятию:'))
        print(withdraw_money(person, count))


def test():
    error = 1
    pattern_card = '[0-9]{16}'
    pattern_password = '[0-9]{4}'
    while (error == 1):
        error = 0
        card_number = input('Введите номер карты:')

        card_data = re.match(pattern_card, card_number)
        if len(card_number) != 16:
            print('Номер карты введен не корректно! Номер содержит 16 цифр!')
            error = 1
            continue
        if card_data == None:
            print('Номер карты введен не корректно! Вводить только цифры!')
            error = 1
            continue

        pin_code = input('Введите пин код:')

        password_data = re.match(pattern_password, pin_code)
        if len(pin_code) != 4:
            print('Пароль введен не корректно! Пароль содержит 4 цифры!!')
            error = 1
            continue


        if password_data == None:
            print('Пароль введен не корректно! Вводить только цифры!')
            error = 1

    if error == 0:
        return card_number, pin_code


def start():
    choice = 0
    while choice != 3:
        card_number, pin_code = test()
        card_number = int(card_number)
        pin_code = int(pin_code)
        person = get_person_by_card(card_number)
        if person and is_pin_valid(person, pin_code):
            while True:
                choice = int(input('Выберите пункт:\n'
                                   '1. Проверить баланс\n'
                                   '2. Снять деньги\n'
                                   '3. Выход\n'
                                   '---------------------\n'
                                   'Ваш выбор:'))
                if choice == 3:
                    print('До свидания!')
                    break
                elif choice == 1 or choice == 2:
                    process_user_choice(choice, person)
                else:
                    print('Неверный номер действия!')
        else:
            print('Номер карты или пин код введены не верно!')


start()


# Вариант с одновременным вводом карты и пароля


# def test():
#     error = 1
#     pattern_card = '[0-9]{16}'
#     pattern_password = '[0-9]{4}'
#     while (error == 1):
#         try:
#             card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()
#             error = 0
#         except UnboundLocalError:
#             print('Данные введены не корректно! Вводить через пробел!')
#             error = 1
#             continue
#         except ValueError:
#             print('Данные введены не корректно! Вводить через пробел!')
#             error = 1
#             continue
#
#         card_data = re.match(pattern_card, card_number)
#         if len(card_number) != 16:
#             print('Номер карты введен не корректно! Номер содержит 16 цифр!')
#             error = 1
#             continue
#         if card_data == None:
#             print('Номер карты введен не корректно! Вводить только цифры!')
#             error = 1
#             continue
#
#         password_data = re.match(pattern_password, pin_code)
#         if len(pin_code) != 4:
#             print('Пароль введен не корректно! Пароль содержит 4 цифры!!')
#             error = 1
#             continue
#
#         if password_data == None:
#             print('Пароль введен не корректно! Вводить только цифры!')
#             error = 1
#
#     if error == 0:
#         return card_number, pin_code
#
#
# start()
