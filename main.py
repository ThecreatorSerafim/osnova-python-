from greetings import say_hello, say_bye
from math_tools import add, multiply

name = input("Введите имя: ")

say_hello(name)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result_add = add(num1, num2)
result_multiply = multiply(num1, num2)

print("Сумма: ", result_add)
print("Произведение: ", result_multiply)

say_bye(name)