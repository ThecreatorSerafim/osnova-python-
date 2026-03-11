#alien_0 = {"color": "green", "points": 5}
#new_points = alien_0["points"]
#print(f'ВЫ заработали {new_points} очков!')
#print(alien_0)
#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)

#Словарь в языке Python представляет собой совокупность пар "ключ-значение"

#alien_0 = {}
#alien_0['color'] = "green"
#alien_0['points'] = 5
#print(alien_0)

#alien_0 = {'color': "green"}
#print(f"Пришелец имеет {alien_0['color']} цвет")
#alien_0['color'] = "желтый"
#print(f'Теперь пришелец имеет {alien_0["color"]} цвет')

#alien_0 = {'x_position': 0, "y_position": 25, "speed": 'medium'}
#print(f"Изначальная позиция: {alien_0['x_position']}")
#if alien_0["speed"] == 'slow':
#    x_increment = 1
#elif alien_0["speed"] == "medium":
#   x_increment = 2
#else:
#    x_increment = 3
#
#alien_0['x_position'] = alien_0["x_position"] + x_increment
#print(f"Новая позиция: {alien_0['x_position']}")

#del alien_0['points']
#print(alien_0)

#любимые_языки_программирования = {
#    "vasya": "Python",
#    "sasha": "JavaScript",
#    "klara": "C++",
#    "philya": "ruby",
#    } 
#язык = любимые_языки_программирования['vasya'].title()
#print(f"Любимй язык программирования Васи это - {язык}.")


person = {"first_name": "Федя", "last_name": "Федотов", "age": 13, "city": "Орел", "poselok": "Гати"}
print(f"Имя моего лучшего друга - {person['first_name']}.")
print(f"А его фамилия это - {person['last_name']}.")
print(f"Ему как и мне {person['age']} лет.")
print(f"Он живет в городе {person['city']}, но по факту в за городом в {person['poselok']}.")

































