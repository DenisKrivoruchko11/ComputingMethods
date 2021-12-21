from functools import reduce
from math import sin, sqrt

from Task5.Task5 import get_xs, get_a_k


def get_result(f, a_k, xs):
    return reduce(lambda v, k: v + a_k[k] * f(xs[k]), range(len(a_k)), 0)


def main():
    def f(x):
        return sin(x)

    def p(x):
        return 1 / sqrt(x)

    # def part1(f_info, p_info, )

    print("Лабораторная работа 6. \n "
          "Приближённое вычисление интегралов при помощи КФ НАСТ. \n "
          "Вариант 3. (f(x) = sin(x), p(x) = 1 / sqrt(x), [a, b] = [0, 1] \n")
    a = float(input("Введите левый конец отрезка интегрирования"))
    b = float(input("Введите правый конец отрезка интегрирования"))
    n = int(input("Введите число узлов"))
    m = int(input("Введите число промежутков дробления"))

    xs = get_xs(-1, 1, n, 10 ** (-12), 10000)
    a_k = get_a_k(n, xs)

    q = (b - a) / 2
    ys = list(map(lambda x: a + q * (x + 1), xs))
    b_k = list(map(lambda k: k * q, a_k))

    print(f"N = {n}, m = {m}")
    print("{:<30} {:<30}".format("Узел", "Коэффициент"))
    for i in range(len(ys)):
        print("{:<30} {:<30}".format(ys[i], b_k[i]))
    print("\n")

    splitting = list(map(lambda j: (a + j * (b - a) / m, a + (j + 1) * (b - a) / m), range(m)))

    result = reduce(lambda v, s: v + get_result(lambda x: p(x) * f(x),
                                                list(map(lambda k: k * (s[1] - s[0]) / (b - a), b_k)),
                                                list(map(lambda x: s[0] + (s[1] - s[0]) / (b - a) * (x - a), ys))),
                    splitting,
                    0)

    print(f"Результат = {result}, Погрешность = {abs(result - 0.6205366034467622036163048463307930151490187776648934)}")

    mu_k = list(map(lambda k: get_result(lambda x: p(x) * x ** k, b_k, ys), range(4)))


if __name__ == "__main__":
    main()
