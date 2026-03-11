"""
level = int(input("Уровень героя: "))
has_key = input("У вас есть ключ?: ") == "да"
has_scroll = input("У вас есть свиток?: ") == "да"
if (has_key or has_scroll )and level > 5:
    print("Проход открыт")
else:
    print("Проход закрыт")
"""
"""
weight = int(input("Введите вес посылки: "))
if weight <= 2:
    print("Иди пешком")
elif weight <= 10:
    print("На велосиеде")
else:
    print("На машине")
"""
while True:
    password = input("Введите пароль: ")
    special_chars = "!@#$%&*."
    has_digit = False
    has_special = False
    has_upper = False
    for c in password:
        if c.isdigit():
            has_digit = True
        if c.isupper():
            has_upper = True
        if c in special_chars:
            has_special = True
    if len(password) >= 8 and has_digit and has_upper and has_special:
        print("Пароль надежен")
    else:
        print("Пароль не надежен")

    
