from math import exp

fs = [(lambda x: 10, lambda x: 10 * x),
      (lambda x: x + 2, lambda x: x ** 2 / 2 + 2 * x),
      (lambda x: (-1.5) * x ** 2 + 13 * x - 0.75, lambda x: -0.5 * x ** 3 + 6.5 * x ** 2 - 0.75 * x),
      (lambda x: 16.8 * x ** 3 + 2.1 * x ** 2 - 290 * x, lambda x: 4.2 * x ** 4 + 0.7 * x ** 3 - 145 * x ** 2),
      (lambda x: (-0.6718) * exp(x) * x, lambda x: (-0.6718) * (x - 1) * exp(x))]


def output(r):
    def out(m, cur):
        print(f"КФ {m}.")
        if len(cur[0]) == 5:
            f = "{:<40} {:<30} {:<30} {:<30} {:<30} {:<20}"
            print(f.format("f(x)", "J", "J при m * l", "Погрешность при m * l", "J по Рунге", "Погрешность по Рунге"))
            print(f.format("10", cur[0][0], cur[0][1], cur[0][2], cur[0][3], cur[0][4]))
            print(f.format("x + 2", cur[1][0], cur[1][1], cur[1][2], cur[1][3], cur[1][4]))
            print(f.format("-1.5 * x ^ 2 + 13 * x - 0.75", cur[2][0], cur[2][1], cur[2][2], cur[2][3], cur[2][4]))
            print(f.format("16.8 * x ^ 3 + 2.64 * x ^ 2 - 290 * x",
                           cur[3][0], cur[3][1], cur[3][2], cur[3][3], cur[3][4]))
            print(f.format("-0.6718 * exp(x) * x", cur[4][0], cur[4][1], cur[4][2], cur[4][3], cur[4][4]))
        else:
            f = "{:<40} {:<30} {:<30} {:<20}"
            print(f.format("f(x)", "J", "J приближенное", "Погрешность"))
            print(f.format("10", cur[0][0], cur[0][1], cur[0][2]))
            print(f.format("x + 2", cur[1][0], cur[1][1], cur[1][2]))
            print(f.format("-1.5 * x ^ 2 + 13 * x - 0.75", cur[2][0], cur[2][1], cur[2][2]))
            print(f.format("16.8 * x ^ 3 + 2.64 * x ^ 2 - 290 * x", cur[3][0], cur[3][1], cur[3][2]))
            print(f.format("-0.6718 * exp(x) * x", cur[4][0], cur[4][1], cur[4][2]))
        print("\n")

    out("левых прямоугольников", r[0])
    out("средних прямоугольников", r[1])
    out("правых прямоугольников", r[2])
    out("трапеций", r[3])
    out("Симпсона", r[4])
    if len(r) == 6:
        out("3/8", r[5])
