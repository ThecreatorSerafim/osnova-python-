while True:
    print()
    print()
    print()

    print("Привет! Это игра 'Кто хочет стать миллионером!'")
    print("Как тебя зовут?")
    name = input("Ответ - ")
    
    print()
    print()
    print()

    print("Очень приятно!", name)
    print("Итак, первый вопрос на тысячу рублей")

    print()
    print()
    print()

    bank = 0

    print("Через сколько лет будет 2045 год?")
    print("Варианты ответов: ")
    print("A. 20")
    print("B. 333")
    print("С. 19")
    print("D. 18")

    print()
    print()
    print()


    ans1 = input("Ответ - ")

    if ans1 == "с" or ans1 == "С":
        print("это правильный ответ")
        bank += 1000
        print("твой банк: " + str(bank))
    else:
        print("К сожалению, ответ  неправильный(((")
        print("Игра окончена")
        print("Твой банк: " + str(bank))
        break

    print()
    print()
    print()

    print("Вопрос на 5000 тысяч рублей")
    print("Когда произошло крещение Руси?")
    print("A. 345")
    print("В. 988")
    print("С. 1000")
    print("Д.100")

    ans2 = input("Ответ - ")

    if ans2 == "В" or ans2 == "в":
        print("это правильный ответ")
        bank += 5000
        print("твой банк: " + str(bank))
    else:
        print("К сожалению, ответ  неправильный(((")
        print("Игра окончена")
        print("Твой банк: " + str(bank))
        break

    print()
    print()
    print()

    print("Финальный вопрос на 10000!!!")
    print("Сколько лет бы вам было, если бы вы родились 34 года назад?")
    print("А. 20")
    print("В. 34")
    print("С. 12")
    print("Д. 56")

    ans3 = input("Ответ - ")

    if ans3 == "В" or ans3 == "в":
        print("это правильный ответ")
        bank += 10000
        print("твой банк: " + str(bank))
    else:
        print("К сожалению, ответ  неправильный(((")
        print("Игра окончена")
        print("Твой банк: " + str(bank))

    print("Поздравляю!!1!!!!")


        
