# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calculate_damage(self, armor_defend):
        return self.damage // armor_defend

    def attack(self, defend):
        damage = self._calculate_damage(defend.armor)
        defend.health -= damage


class Player(Person):
    pass


class Enemy(Person):
    pass


class Battle:

    def fight(player, enemy):
        last_attacker = player
        while player.health > 0 and enemy.health > 0:
            if last_attacker == player:
                player.attack(enemy)
                last_attacker = enemy
            else:
                enemy.attack(player)
                last_attacker = player

        if player.health > 0:
            print('Игрок победил!')
        else:
            print('Враг победил!')


player = Player(100, 25, 1.5)
enemy = Enemy(100, 30, 1.2)

Battle.fight(player, enemy)
