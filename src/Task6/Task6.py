from functools import reduce
from math import sin, sqrt
from numpy import arange
from Task5.Task5 import get_xs, get_a_k


I = 0.62053660344676220361630484633079301514901877766489


def get_result(f, a_k, xs):
    return reduce(lambda v, k: v + a_k[k] * f(xs[k]), range(len(a_k)), 0)


def roots_separation(f, a, b, n):
    h = (b - a) / n
    return reduce(lambda v, i: (v[0] + ([(v[1], i)] if f(v[1]) * f(i) < 0 else []), i),
                  arange(a + h, b, h), ([], a))[0]


def bisection(f, x1, x2, eps):
    c = (x1 + x2) / 2
    return (bisection(f, x1, c, eps) if c - x1 > 2 * eps else (x1 + c) / 2) if f(x1) * f(c) <= 0 else \
        (bisection(f, c, x2, eps) if x2 - c > 2 * eps else (c + x2) / 2)


def composite_gauss(a, b, f, p):
    print("\n_____________________")
    print("Составная КФ Гаусса \n")
    n = int(input("Введите число узлов: \n"))
    m = int(input("Введите число промежутков дробления: \n"))

    xs = get_xs(-1, 1, n, 10 ** (-12), 10000)
    a_k = get_a_k(n, xs)

    q = (b - a) / 2
    ys = list(map(lambda x: a + q * (x + 1), xs))
    b_k = list(map(lambda k: k * q, a_k))

    print(f"\nN = {n}, m = {m}")
    print("{:<30} {:<30}".format("Узел", "Коэффициент"))
    for index in range(len(ys)):
        print("{:<30} {:<30}".format(ys[index], b_k[index]))

    splitting = list(map(lambda j: (a + j * (b - a) / m, a + (j + 1) * (b - a) / m), range(m)))

    result = reduce(lambda v, s: v + get_result(lambda x: p(x) * f(x),
                                                list(map(lambda k: k * (s[1] - s[0]) / (b - a), b_k)),
                                                list(map(lambda x: s[0] + (s[1] - s[0]) / (b - a) * (x - a), ys))),
                    splitting,
                    0)

    print(f"\nR = {result}, |R - I| = {abs(result - I)}")

    return result


def gauss_type(a, b, f, p):
    print("\n_____________________")
    print("КФ типа Гаусса \n")

    m = int(input("\nВведите количество разбиений для вычисления моментов с помощью СКФ средних прямоугольников: \n"))

    xs = list(map(lambda i: a + i * (b - a) / m, range(m + 1)))
    h = (b - a) / m
    qs = list(map(lambda m_f: reduce(lambda v, i: v + m_f(xs[i] + h / 2), range(0, m), 0),
                  list(map(lambda i: lambda x: p(x) * x ** i, range(4)))))
    mu_k = list(map(lambda i: h * qs[i], range(4)))

    """mu_k = list(map(lambda i: reduce(
        lambda v, s: v + get_result(lambda x: p(x) * x ** i,
                                    list(map(lambda k: k * (s[1] - s[0]) / (b - a), b_k)),
                                    list(map(lambda x: s[0] + (s[1] - s[0]) / (b - a) * (x - a), ys))),
        list(map(lambda j: (a + j * (b - a) / m, a + (j + 1) * (b - a) / m), range(m))),
        0), range(4)))"""

    print("\nМоменты:")
    print("{:<20} {:<30}".format("k", "mu_k"))
    for index in range(len(mu_k)):
        print("{:<20} {:<30}".format(index, mu_k[index]))
    print("\n")

    a_1 = (mu_k[0] * mu_k[3] - mu_k[2] * mu_k[1]) / (mu_k[1] ** 2 - mu_k[2] * mu_k[0])
    a_2 = (mu_k[2] ** 2 - mu_k[3] * mu_k[1]) / (mu_k[1] ** 2 - mu_k[2] * mu_k[0])

    print(f"Ортогональный многочлен: x^2 + {a_1} * x + {a_2}")
    rs = list(map(lambda cur: bisection(lambda x: x ** 2 + a_1 * x + a_2, cur[0], cur[1], 10 ** (-12)),
                  roots_separation(lambda x: x ** 2 + a_1 * x + a_2, a, b, 1000)))

    ys = [(mu_k[1] - mu_k[0] * rs[1]) / (rs[0] - rs[1]), (mu_k[1] - mu_k[0] * rs[0]) / (rs[1] - rs[0])]

    print("{:<30} {:<30}".format("Узел", "Коэффициент"))
    for index in range(len(ys)):
        print("{:<30} {:<30}".format(rs[index], ys[index]))

    result = get_result(lambda x: x ** 3, ys, rs)
    print(f"\nПроверка для x^3: R = {result}, |R - 2/7| = {abs(result - 2 / 7)}")

    result = get_result(f, ys, rs)
    print(f"\nЗадача из условия (f(x) = sin(x), p(x) = 1 / sqrt(x), [a, b] = [0, 1]): "
          f"R = {result}, |R - I| = {abs(result - I)}")

    return result


def main():
    def f(x):
        return sin(x)

    def p(x):
        return 1 / sqrt(x)

    print("Лабораторная работа 6. \n"
          "Приближённое вычисление интегралов при помощи КФ НАСТ. \n"
          "Вариант 3. (f(x) = sin(x), p(x) = 1 / sqrt(x), [a, b] = [0, 1]")

    a = 0  # int(input("Введите нижний предел интегрирования: \n"))
    b = 1  # int(input("Введите верхний предел интегрирования: \n"))

    composite_result = composite_gauss(a, b, f, p)
    gauss_type_result = gauss_type(a, b, f, p)

    print("\n_____________________ \n"
          "Сводная таблица: \n")

    form = "{:<30} {:<30} {:<30}"
    print(form.format("Метод", "R", "|R - I|"))
    print(form.format("Составная КФ Гаусса", composite_result, abs(composite_result - I)))
    print(form.format("КФ типа Гаусса", gauss_type_result, abs(gauss_type_result - I)))


if __name__ == "__main__":
    main()
