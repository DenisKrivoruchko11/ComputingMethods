from functools import reduce
from math import exp
from Task4.common import fs, output


def left_rectangle(h, f0, w):
    return h * (f0 + w)


def middle_rectangle(h, q):
    return h * q


def right_rectangle(h, fn, w):
    return h * (w + fn)


def trapezoid(h, z, w):
    return h / 2 * (z + 2 * w)


def simpson(h, z, w, q):
    return h / 6 * (z + 2 * w + 4 * q)


def theoretical(a, b, n):
    def t(c, d):
        return c * exp(b) * (b - a) * (h ** (d + 1))

    form = "{:<30} {:<30} {:<30} {:<30}"

    h = (b - a) / n
    xs = list(map(lambda i: a + i * (b - a) / n, range(n + 1)))

    w = reduce(lambda v, i: v + exp(xs[i]), range(1, n), 0)
    q = reduce(lambda v, i: v + exp(xs[i] + h / 2), range(0, n), 0)
    z = exp(a) + exp(b)

    j = exp(b) - exp(a)
    r = list(map(lambda i: (i, abs(j - i)), [left_rectangle(h, exp(a), w), middle_rectangle(h, q),
                                             right_rectangle(h, exp(b), w), trapezoid(h, z, w), simpson(h, z, w, q)]))

    print(f"Результаты для функции exp(x) на отрезке [{a}, {b}] (J = {j}): ")
    print(form.format("КФ", "J приближенное", "Погрешность", "Теоретическая погрешность"))
    print(form.format("Левых прямоугольников", r[0][0], r[0][1], t(0.5, 0)))
    print(form.format("Средних прямоугольников", r[1][0], r[1][1], t(1 / 24, 1)))
    print(form.format("Правых прямоугольников", r[2][0], r[2][1], t(0.5, 0)))
    print(form.format("Трапеций", r[3][0], r[3][1], t(1 / 12, 1)))
    print(form.format("Симпсона", r[4][0], r[4][1], t(1 / 2880, 3)))


def main(a, b, n):
    h = (b - a) / n

    xs = list(map(lambda i: a + i * (b - a) / n, range(n + 1)))
    ws = list(map(lambda f: reduce(lambda v, i: v + f[0](xs[i]), range(1, n), 0), fs))
    qs = list(map(lambda f: reduce(lambda v, i: v + f[0](xs[i] + h / 2), range(0, n), 0), fs))
    zs = list(map(lambda f: f[0](a) + f[0](b), fs))

    results = [[] for _ in range(5)]
    for k in range(len(fs)):
        j = fs[k][1](b) - fs[k][1](a)

        l_r = left_rectangle(h, fs[k][0](a), ws[k])
        m_r = middle_rectangle(h, qs[k])
        r_r = right_rectangle(h, fs[k][0](b), ws[k])
        t = trapezoid(h, zs[k], ws[k])
        s = simpson(h, zs[k], ws[k], qs[k])

        results[0].append((j, l_r, abs(j - l_r)))
        results[1].append((j, m_r, abs(j - m_r)))
        results[2].append((j, r_r, abs(j - r_r)))
        results[3].append((j, t, abs(j - t)))
        results[4].append((j, s, abs(j - s)))

    return results


if __name__ == "__main__":
    print("Задача 4.2: приближенное вычисление интеграла по составным квадратурным формулам \nВариант 3")

    A = float(input("Введите нижний предел интегрирования a: "))
    B = float(input("Введите верхний предел интегрирования b: "))
    N = int(input("Введите n: "))
    rs = main(A, B, N)

    output(rs)

    print("Рассчет теоретической погрешности для функции exp(x)")
    A = float(input("Введите нижний предел интегрирования a: "))
    B = float(input("Введите верхний предел интегрирования b: "))
    N = int(input("Введите n: "))
    theoretical(A, B, N)
