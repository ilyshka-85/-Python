"""

1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""






def division(first_obj, second_obj):
    try:
        return first_obj/second_obj
    except ZeroDivisionError:
        return "0"
try:
    first_numb = int(input("4"))
    second_numb = int(input("9"))
    print(division(first_numb, second_numb))
except ValueError:
    print("Пожалуйста, вводите только числа")
