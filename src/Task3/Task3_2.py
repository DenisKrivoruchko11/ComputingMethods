from math import exp
from numpy import arange


def get_info(t, h, df, df2):
    def cur_info(cur):
        def d(i, o):
            f = list(t.values()).__getitem__ if o == 1 else lambda j: d(j, o - 1)
            return ((-3 * f(i) + 4 * f(i + 1) - f(i + 2)) if i == 0 else
                    (f(i + 1) - f(i - 1)) if i < len(t) - 1 else
                    (3 * f(i) - 4 * f(i - 1) + f(i - 2))) / (2 * h)

        d1 = d(cur, 1)
        d2 = d(cur, 2)
        ks = list(t)
        return cur, t.get(ks[cur]), d1, abs(df(ks[cur]) - d1), d2, abs(df2(ks[cur]) - d2)

    return list(map(lambda i: cur_info(i), range(len(t))))


def main():
    def f(x):
        return exp(6 * x)

    print("Задача обратного интерполирования \nВариант 3")

    while True:
        m = int(input('Введите число значений в таблице m+1: ')) - 1
        a = float(input('Введите левый конец отрезка a: '))
        h = float(input('Введите шаг h: '))

        table = dict(map(lambda i: (i, f(i)), arange(a, a + h * m, h)))
        print(f"Полученная таблица в формате (x, f(x)): \n{table}")

        print(f"Результат в формате (x, f(x), f'(x), |f'(x)_Т - f'(x)_ЧД|, f''(x), |f''(x)_Т - f''(x)_ЧД|: \n"
              f"{get_info(table, h, lambda x: 6 * f(x), lambda x: 36 * f(x))}")

        if input("Для выхода нажмите 1. Для продолжения --- любую клавишу.") == "1":
            break


if __name__ == '__main__':
    main()

