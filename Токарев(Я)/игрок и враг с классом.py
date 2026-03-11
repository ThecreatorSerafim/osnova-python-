class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, damage):
        self.hp -= damage
        print(self.name, "получил урон", damage)

class Player:
    def ___init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name, "атакует", enemy.name)
        enemy.take_damage(20)

enemy = Enemy("Монстр", 50)
player = Player("Герой")

player.attack(enemy)
