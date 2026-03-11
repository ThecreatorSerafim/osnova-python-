import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def __str__(self):
        return f"{self.name}: HP {self.hp}/100"

    def is_alive(self):
        return self.hp > 0

    def hit(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(self.name, "получил урон:", damage)

    def attack(self, enemy):
        damage = random.randint(12, 20)
        print(self.name, "атакует", enemy.name, "на", damage)
        enemy.take_damage(damage)

class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f"{self.name}: HP {self.hp}/50"

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(self.name, "теперь имеет HP:", self.hp)

    def attack(self, player):
        damage = random.randint(7, 13)
        print(self.name, "бьёт", player.name, "на" , damage)
        player.hit(damage)

def game():
    print("=== Мини-RPG === ")
    name = input("Имя героя: ")
    player = Player(name)
    monster = Monster("Слизень", 50)
    print("\nСтарт: ")
    print(player)
    print(monster)

    while player.is_alive and monster.is_alive():
        input("\nНажми Enter, что бы атаковать")
        player.attack(monster)

        if monster.is_alive():
            monster.attack(player)

        print("\nСостояние: ")
        print(player)
        print(monster)

    if player.is_alive():
        print("\nПобеда))))")
    else:
        print("\nПоражение((((")

game()









        
