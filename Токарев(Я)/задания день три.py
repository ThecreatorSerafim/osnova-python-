#Задание №1
"""
inventory = ["меч", "щит", "зелье", "лук"]
print(len(inventory))
for item in inventory:
    print(item)
print(inventory[0])
print(inventory[3])
"""

#Задание №2
"""
spisok = ["лук", "меч", "щит", "зелье"]
a =  input("Что вы хотите купить?: ")
if a in spisok:
    print("Покупка успешна")
else:
    print("Товара нет")
"""

#Задание №3
"""
spisok = ["сломанный", "лук", "щит", "зелье", "кока колла"]
spisok.remove('сломанный')
print(spisok)
"""

#Задание №4

enemy1 = 10
enemy2 = 20
enemy3 = 52
hit1 = 0
hit2 = 0
hit3 = 0
while enemy1 > 0:
    enemy1 -= 2
    hit1 += 1
print("Для первого надо", hit1 ,"ударов")
while enemy2 > 0:
    enemy2 -= 2
    hit2 += 1
print("Для второго надо", hit2 ,"ударов")
while enemy3 > 0:
    enemy3 -= 2
    hit3 += 1
print("Для третьего надо", hit3, "ударов")


#Задание №5


