def symma(a, b, c):
    d = [a, b, c]
    d.remove(min(a, b, c))
    return sum(d)


print(symma(c=int(input("Введите целое число: ")),
            b=int(input("Введите целое число: ")),
            a=int(input("Введите целое число: "))))
