# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


def attack(person1, person2):
    person2['health'] = person2['health'] - person1['damage']
    return person2


player = {'name' : input('Введите имя сущности player:'), 'health' : 100, 'damage' : 25}
enemy = {'name' : input('Введите имя сущности enemy'), 'health' : 100, 'damage' : 30}

attack(player,enemy)
attack(player,enemy)
attack(enemy,player)

print(player)
print(enemy)