
"""
prompt = "\nНапиши мне что нибудь и я повторю это: "
prompt += "\nНабери слово 'выход' для завершения проги.: "
message = ""
active = True #это флаг!
while active:
    message = input(prompt)
    if message == "выход":
        active = False
    elif message == "quit":
        active = False
    elif message == "уйти":
        active = False
    else:
        print(message)
"""

"""
prompt = "\nВведите название города в котором вы были: "
prompt += "\nНаберите выход для завершения программы: "

while True:
    city = input(prompt)

    if city == "выход":
        break
    else:
        print(f"Я бывал(а) в прекрасном городе {city.title()}!")
"""
"""
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
         continue
    print(current_number)
"""

x = 1
while x <= 5:
    print(x)
    x += 1










    
