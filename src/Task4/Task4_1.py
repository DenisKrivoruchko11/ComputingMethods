from Task4.common import fs, output


def rectangle(f, a, b, m):
    return (b - a) * f(a if m == 0 else (a + b) / 2 if m == 1 else b)


def trapezoid(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))


def simpson(f, a, b):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))


def three_eight(f, a, b):
    h = (b - a) / 3
    return (b - a) * (1 / 8 * f(a) + 3 / 8 * f(a + h) + 3 / 8 * f(a + 2 * h) + 1 / 8 * f(b))


def main():
    def compute(m):
        return list(map(lambda f: (lambda r: (f[1](b) - f[1](a), r, abs(f[1](b) - f[1](a) - r)))(m(f[0], a, b)), fs))

    print("Задача 4.1: приближенное вычисление интеграла по квадратурным формулам \nВариант 3")
    a = float(input("Введите нижний предел интегрирования a: "))
    b = float(input("Введите верхний предел интегрирования b: \n"))

    output([compute(lambda p1, p2, p3: rectangle(p1, p2, p3, 0)), compute(lambda p1, p2, p3: rectangle(p1, p2, p3, 1)),
            compute(lambda p1, p2, p3: rectangle(p1, p2, p3, 2)), compute(trapezoid), compute(simpson),
            compute(three_eight)])


if __name__ == "__main__":
    main()
