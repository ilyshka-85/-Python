"""

7. Продолжить работу над заданием. В программу должна попадать строка из слов,
разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().

"""
def int_func(string):
    return string.title()


print(int_func("text"))
def title_func(string):
    list_title = []
    lst = string.split()
    for el in lst:
        list_title.append(int_func(el))
    print(*list_title)

title_func("каждое слово теперь будет с заглавной буквы")