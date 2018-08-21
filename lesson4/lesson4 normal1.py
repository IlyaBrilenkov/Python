# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @,
#  потом текст, допускаются цифры, точка, ru или org или com.

import re

name = input('Введите имя:')
surname = input('Введите фамилию:')
email = input('Введите email:')

pattern_name = '[А-ЯA-Z][a-zа-я]+'
pattern_email = '[a-z_0-9]+@[a-z0-9]+\.(ru|org|com)'

test_name = re.match(pattern_name, name)
if test_name == None:
    print('Неверно указано имя')

test_surname = re.match(pattern_name, surname)
if test_surname == None:
    print('Неверно указана фамилия')

test_email = re.match(pattern_email, email)
if test_email == None:
    print('Неверно указан email')
