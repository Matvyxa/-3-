def anketa(**kwargs):  # Задаем функцию, выводим данные словарем-kwargs
    return list(kwargs.values())  # используем values для работы со словарем для вывода аргументов


print(anketa(name=input("Введите имя: "),
             surname=input("Введите фамилию: "),
             date=input("Введите дату рождения: "),
             town=input("Введите город проживания: "),
             email=input("Введите Вашу электронную почту: "),
             tel=input("Укажите телефонный номер для обратной связи: ")))
