"""

2. Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

"""

secs = int(input("3600"))
hours = secs / 3600
minutes = secs / 60

print(f"1.0 : 60.0 : 3600 - {hours} : {minutes} : {secs}")
