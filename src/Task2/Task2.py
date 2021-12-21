from math import exp
from functools import reduce


def lagrange(t, x):
    return reduce(
        lambda c, i: c + t.get(i) * (lambda p: p[0] / p[1])(reduce(lambda v, k: (v[0] * (x - k) if i != k else v[0],
                                                                                 v[1] * (i - k) if i != k else v[1]),
                                                                   t, (1, 1))),
        t, 0)


def newton(t, x):
    def get_result(k):
        s = 1
        for m in range(k):
            s *= x - ks[m]

        return (get_result(k - 1) if k > 0 else 0) + s * dif[k][0]

    ks = list(t)
    vs = list(t.values())
    n = len(t) - 1

    dif = list(map(lambda _: list(map(lambda _: 0, range(n + 1))), range(n + 1)))
    for i in range(n + 1):
        for j in range(n + 1 - i):
            dif[i][j] = vs[j] if i == 0 else (dif[i - 1][j + 1] - dif[i - 1][j]) / (ks[j + i] - ks[j])

    return get_result(n)


def main():
    def f(x):
        return exp(x) - x

    print("Задача алгебраического интерполирования. Интерполяционный многочлен в форме Ньютона и в форме Лагранжа. \n"
          "Вариант 3.")

    m = int(input('Введите число значений в таблице m+1: ')) - 1
    a = float(input('Введите левый конец отрезка a: '))
    b = float(input('Введите правый конец отрезка b: '))

    table = dict(map(lambda i: (a + i * (b - a) / m, f(a + i * (b - a) / m)), range(m + 1)))

    print(f"Полученная таблица в формате (x, f(x)): {table}")

    while True:
        while True:
            p = float(input(f'Введите точку интерполирования x ({a}<=x<={b}, x не из таблицы): '))
            if a <= p <= b and p not in table.keys():
                break
            print('Введена некорректная точка интерполирования')

        while True:
            n = int(input(f'Введите степень интерполяционного многочлена n (n<={m}): '))
            if n <= m:
                break
            print('Введена некорректная степень интерполяционного многочлена')

        t = dict(sorted(table.items(), key=lambda i: abs(i[0] - p))[:n + 1])
        l_r = lagrange(t, p)
        n_r = newton(t, p)

        print(f"Выбранные узлы: {t} \n"
              f"Результат по Лагранжу: {l_r} \nПогрешность по Лагранжу: {abs(l_r - f(p))} \n"
              f"Результат по Ньютону: {n_r} \nПогрешность по Ньютону: {abs(n_r - f(p))}")

        if input("Для выхода нажмите 1. Для продолжения --- любую клавишу.") == "1":
            break


if __name__ == '__main__':
    main()
