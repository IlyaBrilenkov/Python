# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def shield(person1, person2):
    damage_cor = person1['damage'] / person2['armor']
    return damage_cor


def attack(person2):
    person2['health'] = person2['health'] - damage_cor
    return person2


def data():
    player = {}
    with open('player.txt') as player1:
        for i in player1.readlines():
            key, val = i.strip().split(':')
            player[key] = val
    enemy = {}
    with open('enemy.txt') as player2:
        for i in player2.readlines():
            key, val = i.strip().split(':')
            enemy[key] = val
    return (player, enemy)


player1 = input('Введите имя сущности player:')
player2 = input('Введите имя сущности enemy:')

player = {'name': player1, 'health': 100, 'damage': 25, 'armor': 1.2}
enemy = {'name': player2, 'health': 100, 'damage': 30, 'armor': 1.2}

player = {'name': player1, 'health': 100, 'damage': 25, 'armor': 1.2}
with open('player.txt', 'w', encoding='UTF-8') as player1:
    for key, val in player.items():
        player1.write('{}:{}\n'.format(key, val))

enemy = {'name': player2, 'health': 100, 'damage': 30, 'armor': 1.2}
with open('enemy.txt', 'w', encoding='UTF-8') as player2:
    for key, val in player.items():
        player2.write('{}:{}\n'.format(key, val))

data()

while player['health'] > 0 and enemy['health'] > 0:
    damage_cor = shield(player, enemy)
    attack(enemy)
    if enemy['health'] <= 0:
        print(f'Победитель: {player["name"]}, осталось единиц здоровья: {player["health"]}')
    else:
        damage_cor = shield(enemy, player)
        attack(player)
        if player['health'] <= 0:
            print(f'Победитель: {enemy["name"]}, осталось единиц здоровья: {enemy["health"]}')

