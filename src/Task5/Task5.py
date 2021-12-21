from functools import reduce
from math import pi, sin, sqrt, cos


def roots_separation(f, a, b, n):
    h = (b - a) / n
    result = []
    for i in range(n):
        l = a + i * h
        r = a + (i + 1) * h
        m = f(l) * f(r)
        if m < 0 or (f(l) == 0):
            result.append((l, r))

    return result


def bisection(f, eps, a, b):
    c = (a + b) / 2
    return (bisection(f, eps, a, c) if c - a > 2 * eps else (a + c) / 2) if f(a) * f(c) <= 0 else \
        (bisection(f, eps, c, b) if b - c > 2 * eps else (c + b) / 2)


def legendre(n, x):
    return 1 if n == 0 else x if n == 1 else (2 * n - 1) / n * legendre(n - 1, x) * x - (n - 1) / n * legendre(n - 2, x)


def get_xs(a, b, n, eps, m):
    def f(x):
        return legendre(n, x)

    result = []
    for p in roots_separation(f, (a + b) / 2, b, m):
        if p[0] == (a + b) / 2 and n % 2 == 1:
            result.append((a + b) / 2)
            continue

        cur = bisection(f, eps, p[0], p[1])
        result.append(cur)
        result.insert(0, (a + b) / 2 - cur)

    return result


def get_a_k(n, xs):
    return list(map(lambda x: 2 * (1 - x ** 2) / (n * (legendre(n - 1, x))) ** 2, xs))


def meller(f, n):
    print("\n")
    xs = list(map(lambda k: cos((2 * k - 1) / (2 * n) * pi), range(1, n + 1)))
    print(f"Узлы КФ Меллера для {n}:")
    for x in xs:
        print(x)
    return pi / n * reduce(lambda v, x: v + f(x), xs, 0)


def main():
    def get_result(f, a_k, xs):
        return reduce(lambda v, k: v + a_k[k] * f(xs[k]), range(len(a_k)), 0)

    def part1():
        a = -1
        b = 1
        eps = 10 ** (-12)
        m = 10000

        xs = list(map(lambda n: get_xs(a, b, n + 1, eps, m), range(8)))
        a_k = list(map(lambda n: get_a_k(n + 1, xs[n]), range(len(xs))))

        for i in range(len(xs)):
            print(f"При N = {i + 1}:")
            print("{:<30} {:<30}".format("Узел", "Коэффициент"))
            for j in range(len(xs[i])):
                print("{:<30} {:<30}".format(xs[i][j], a_k[i][j]))
            print("\n")

        fs = [lambda x: 6 * x ** 5 + 5 * x ** 4 - 4 * x ** 3 - 3 * x ** 2 + 2 * x + 1,
              lambda x: 16 * x ** 7 - 21 * x ** 6 + 3 * x ** 5 - 10 * x ** 4 + 16 * x ** 3 - 6 * x ** 2 + 18 * x - 8,
              lambda x: 2000 * x ** 9 + 77 * x ** 6 - 20 * x ** 3 - 0.7]

        print("{:<20} {:<10} {:<30}".format("Степень многочлена", "N", "Погрешность"))
        print("{:<20} {:<10} {:<30}".format("5", "3", f"{abs(get_result(fs[0], a_k[2], xs[2]) - 2)}"))
        print("{:<20} {:<10} {:<30}".format("7", "4", f"{abs(get_result(fs[1], a_k[3], xs[3]) + 30)}"))
        print("{:<20} {:<10} {:<30}".format("9", "5", f"{abs(get_result(fs[2], a_k[4], xs[4]) - 20.6)}"))
        print("\n")

    def part2():
        def f(x):
            return sqrt(1 - 1 / 2 * ((sin(x)) ** 2))

        a = float(input("Введите левый конец отрезка: \n"))
        b = float(input("Введите правый конец отрезка: \n"))
        eps = 10 ** (-12)
        m = int(input("Введите количество разбиений: \n"))

        print("Функция: sqrt(1 - 1 / 2 * ((sin(x)) ** 2)). Интеграл на отрезке [0, pi/2] = 1.350643881047676")
        for n in [5, 6, 7, 8]:
            print("\n")
            print(f"N = {n}")

            xs = get_xs(-1, 1, n, eps, m)
            a_k = get_a_k(n, xs)

            q = (b - a) / 2
            ys = list(map(lambda x: a + q * (x + 1), xs))
            b_k = list(map(lambda k: k * q, a_k))

            print("{:<30} {:<30}".format("Узел", "Коэффициент"))
            for i in range(len(a_k)):
                print("{:<30} {:<30}".format(xs[i], a_k[i]))

            print(f"J приближенное = {get_result(f, b_k, ys)}")

    def part3():
        print("\n")
        print("КФ Меллера")
        n1 = int(input("Введите N1: \n"))
        n2 = int(input("Введите N2: \n"))
        n3 = int(input("Введите N3: \n"))

        ns = [n1, n2, n3]

        print(f"Результаты по Меллеру: \n")

        for n in ns:
            cur = meller(lambda x: 1 / sqrt(1 - x ** 2), n)
            print("{:<20} {:<40} {:<40}".format("N", "Результат", "Погрешность"))
            print("{:<20} {:40} {:<40}".format(n, cur, abs(cur - pi)))

    part1()
    part2()
    # part3()


if __name__ == "__main__":
    main()
