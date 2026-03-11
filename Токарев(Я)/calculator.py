def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

def delit(a, b):
    return a/b

def ymnosz(a, b):
    return a*b

def show_menu():
    print("Выберите оператор: +, -, /, *")
    print("Введите два числа")

show_menu()

a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
operation = input("Введите знак операции: ")

if operation == "+":
    result = plus(a, b)
elif operation == "-":
    result = minus(a, b)
elif operation == "/":
    result = delit(a, b)
elif operation == "*":
    result = ymnosz(a, b)
else:
    print("Операция недоступна")
print("Результат", result)
