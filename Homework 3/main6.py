"""

6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
и возвращающую их же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

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
