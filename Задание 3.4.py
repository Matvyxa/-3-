def stepen(a, b):  # задаем функцию
    return 1 / a ** abs(b)  # возводим в степень


print(stepen(a=float(input("Введите челое число: ")),
             b=int(input("Введите челое число: "))))
