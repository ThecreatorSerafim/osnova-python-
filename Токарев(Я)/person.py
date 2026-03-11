"""
def build_person(first_name, last_name, age = None):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person
musician = build_person("иоган", "бах", age = 300)
print(musician)
"""

"""
def city_country(city, country):
    name = f"{city}  {country}"
    return name
Town = city_country("Орел", "Россия")
Town1 = city_country("Рим", "Италия")
Town2 = city_country("Париж", "Франция")
print(Town)
print(Town1)
print(Town2)
"""
def make_album(author, name, count_music_roads = None):
    album = {"author": author, "name": name}
    if count_music_roads:
        album["count_music_roads"] = count_music_roads
    return album
albom = make_album("Филлип Киркоров", "Единственная моя", count_music_roads = 1231)
albom1 = make_album("Пошлая Молли", "Мальборо голд", count_music_roads = 1234)
albom2 = make_album("Eric Clapton", "Tears in Heaven", count_music_roads = 1235)
print(albom)
print(albom2)
print(albom1)


