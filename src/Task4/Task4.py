from functools import reduce
from math import exp


def rectangle(f, n, xs, h, m):
    return h * reduce(lambda v, i: v + f(xs[i] + h * m / 2), range(n), 0)


def trapezoid(f, n, xs, h):
    return h / 2 * reduce(lambda v, i: v + f(xs[i]) / (1 + (i % n == 0)), range(n + 1), 0)


def simpson(f, n, xs, h):
    return h / 3 * reduce(lambda v, i: v + f(xs[i]) * (1 if i % n == 0 else 2 + 2 * (i % 2 != 0)), range(n + 1))


def three_eight(f, n, xs, h):
    return h * n / 8 * reduce(lambda v, i: v + f(xs[i]) / (1 + 2 * (i % n == 0)), range(n), 0)


def main():
    def compute(m):
        return list(map(lambda f: (lambda r: (r, abs(f[1](b) - f[1](a) - r)))(m(f[0], n, xs, h)), fs))

    def output(m, r):
        print(f"КФ {m}. \n"
              f"f(x) = 10: {r[0][0]} | Погрешность: {r[0][1]}\n"
              f"f(x) = x+2: {r[1][0]} | Погрешность: {r[1][1]}\n"
              f"f(x) = -1.5 * x ^ 2 + 13 * x - 0.75: {r[2][0]} | Погрешность: {r[2][1]}\n"
              f"f(x) = 16.8 * x ^ 3 + 2.64 * x ^ 2 - 290 * x: {r[3][0]} | Погрешность: {r[3][1]}\n"
              f"f(x) = -0.6718 * exp(x) * x: {r[4][0]} | Погрешность: {r[4][1]}\n")

    fs = [(lambda x: 10, lambda x: 10 * x),
          (lambda x: x + 2, lambda x: x ** 2 / 2 + 2 * x),
          (lambda x: (-1.5) * x ** 2 + 13 * x - 0.75, lambda x: -0.5 * x ** 3 + 6.5 * x ** 2 - 0.75 * x),
          (lambda x: 16.8 * x ** 3 + 2.64 * x ** 2 - 290 * x, lambda x: 4.2 * x ** 4 + 0.84 * x ** 3 - 145 * x ** 2),
          (lambda x: (-0.6718) * exp(x) * x, lambda x: (-0.6718) * (x - 1) * exp(x))]

    print("Задача: приближенное вычисление интеграла по квадратурным формулам \nВариант 3")
    a = float(input("Введите нижний предел интегрирования a: "))
    b = float(input("Введите верхний предел интегрирования b: "))
    n = int(input("Введите n: "))

    h = (b - a) / n
    xs = list(map(lambda i: a + i * h, range(n + 1)))

    output("левого прямоугольника", compute(lambda p1, p2, p3, p4: rectangle(p1, p2, p3, p4, 0)))
    output("среднего прямоугольника", compute(lambda p1, p2, p3, p4: rectangle(p1, p2, p3, p4, 1)))
    output("правого прямоугольника", compute(lambda p1, p2, p3, p4: rectangle(p1, p2, p3, p4, 2)))
    output("трапеции", compute(trapezoid))
    output("Симпсона", compute(simpson))
    output("3/8", compute(three_eight))


if __name__ == "__main__":
    main()
