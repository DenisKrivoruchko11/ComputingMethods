from Task2.Task2 import main as task2
from Task3.Task3_1 import main as task3_1
from Task3.Task3_2 import main as task3_2

if __name__ == "__main__":
    while True:
        t = input("Введите номер задачи: ")
        if t == "2":
            task2()
        elif t == "3_1":
            task3_1()
        elif t == "3_2":
            task3_2()
        else:
            break
