from functools import reduce
from math import exp
from numpy import arange
from Task2.Task2 import lagrange


def method1(t, y):
    return lagrange(dict(zip(t.values(), t)), y)


def method2(t, y, a, b, n, eps):
    def f(x):
        return lagrange(t, x) - y

    def roots_separation():
        h = (b - a) / n
        return reduce(lambda v, i: (v[0] + ([(v[1], i)] if f(v[1]) * f(i) < 0 else []), i),
                      arange(a + h, b, h), ([], a))[0]

    def bisection(x1, x2):
        c = (x1 + x2) / 2
        return (bisection(x1, c) if c - x1 > 2 * eps else (x1 + c) / 2) if f(x1) * f(c) <= 0 else \
               (bisection(c, x2) if x2 - c > 2 * eps else (c + x2) / 2)

    return list(map(lambda p: bisection(p[0], p[1]), roots_separation()))


def main():
    def f(x):
        return exp(x) - x

    print("Задача обратного интерполирования \nВариант 3")

    m = int(input('Введите число значений в таблице m+1: ')) - 1
    a = float(input('Введите левый конец отрезка a: '))
    b = float(input('Введите правый конец отрезка b: '))

    table = dict(map(lambda i: (i, f(i)), arange(a, b, (b - a) / m)))
    print(f"Полученная таблица в формате (x, f(x)): {table}")

    while True:
        while True:
            p = float(input(f'Введите точку для обратного интерполирования F ({f(a)}<=F<={f(b)}, F не из таблицы): '))
            if f(a) <= p <= f(b) and p not in table.values():
                break
            print('Введена некорректная точка интерполирования')

        while True:
            n = int(input(f'Введите степень интерполяционного многочлена n (n<={m}): '))
            if n <= m:
                break
            print('Введена некорректная степень интерполяционного многочлена')

        eps = float(input('Введите eps: '))

        t = dict(sorted(table.items(), key=lambda i: abs(i[1] - p))[:n + 1])

        r1 = method1(t, p)
        r2 = method2(t, p, a, b, n, eps)

        print(f"Результат по первому методу: {r1} \nНевязка: {abs(f(r1) - p)} \n"
              f"Результат по второму методу: {r2} \n"
              f"Невязка: {reduce(lambda v, i: max(abs(f(i) - p), v), r2, abs(f(r2[0]) - p))}")

        if input("Для выхода нажмите 1. Для продолжения --- любую клавишу.") == "1":
            break


if __name__ == '__main__':
    main()
