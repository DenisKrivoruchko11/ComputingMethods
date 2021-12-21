from Task4.Task4_2 import main, output
from Task4.common import fs

if __name__ == "__main__":
    def runge(f, i, d):
        r = d + 1
        temp = L ** r
        return (temp * j_h_l[f][i][1] - j_h[f][i][1]) / (temp - 1)

    print("Задача 4.3: приближенное вычисление интеграла с использованием метода Рунге \nВариант 3")

    A = float(input("Введите нижний предел интегрирования a: "))
    B = float(input("Введите верхний предел интегрирования b: "))
    N = int(input("Введите n: "))

    j_h = main(A, B, N)
    output(j_h)

    L = int(input("Введите l: "))

    j_h_l = main(A, B, N * L)

    j_r = [[] for _ in range(5)]
    for k in range(len(fs)):
        j = fs[k][1](B) - fs[k][1](A)

        l_r = runge(0, k, 0)
        m_r = runge(1, k, 1)
        r_r = runge(2, k, 0)
        t = runge(3, k, 1)
        s = runge(4, k, 3)

        j_r[0].append((j, j_h_l[0][k][1], j_h_l[0][k][2], l_r, abs(j - l_r)))
        j_r[1].append((j, j_h_l[1][k][1], j_h_l[1][k][2], m_r, abs(j - m_r)))
        j_r[2].append((j, j_h_l[2][k][1], j_h_l[2][k][2], r_r, abs(j - r_r)))
        j_r[3].append((j, j_h_l[3][k][1], j_h_l[3][k][2], t, abs(j - t)))
        j_r[4].append((j, j_h_l[4][k][1], j_h_l[4][k][2], s, abs(j - s)))

    output(j_r)
