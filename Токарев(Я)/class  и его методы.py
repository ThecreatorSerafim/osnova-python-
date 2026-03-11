"""
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(self.name, "говорит: мяу")

    def eeat(self):
        print(self.name, "хочет кушац")
        
cat1 = Cat("Барсик", 3)
cat2 = Cat("Васька", 15)
cat3 = Cat("Рыжик", 13)

print(cat1.name)
print(cat1.age)
print(cat2.name)
print(cat2.age)

cat2.meow()
cat1.meow()
cat3.meow()
cat2.eeat()

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(self.name, "лает!!")
        
Dog1 = dog("Бобик", 23)
Dog1.bark()


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)
        print(self.name, "получила среднюю оценку: ")
        
student1 = Student("Аня", [5, 5, 5, 5, 4])
student2 = Student("Ваня", [2, 3, 3, 4, 5])
student3 = Student("Саша", [4, 3, 3, 5, 5])
student4 = Student("Артем", [5, 3, 4 ,5, 4])

print(student1.average())
print(student2.average())
print(student3.average())
print(student4.average())

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def hit(self):
        self.hp -= 10
        print(self.name, "получил урон")

    def heal(self):
        self.hp += 5
        print(self.name, "восстановил хп")

    def show_hp(self):
        print("Здоровье: ", self.hp)

p = Player("Анатолий")
p.hit()
p.hit()
p.hit()
p.heal()
p.heal()
p.show_hp()
"""

    















