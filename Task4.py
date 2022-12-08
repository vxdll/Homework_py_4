# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
#     *Пример:*
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
# *Доп задание: значения коэффициентов от -100 до 100
import random

# Создадим рандомные коэффициенты при помощи рандома
k = int(input("Введите коэффициент k: "))
coefficient = [random.randint(-100, 100) for i in range(0, k + 1)]
print(coefficient)

# Создаем цикл c условиями
x = ""
for i in range(0, k + 1):
    if k - i > 1 and coefficient[i] != 0:
        x = x + f"{coefficient[i]}*x^{k-i} + "
    elif k - i > 1 and coefficient[i] == 0:
        x = x + f"x^{k-i} + "
    elif k - i == 1 and coefficient[i] != 0:
        x = x + f"{coefficient[i]}*x + "
    elif k - i == 0 and coefficient[i] != 0:
        x = x + f"{coefficient[i]} = 0"
    elif k - i == 0 and coefficient[i] == 0:
        x = x + "= 0"
        x = x.replace(" + =", " =")


x = x.replace("+ -", "- ")
print(x)

# записываем в txt файл полученный результат
with open("task4", "w") as data:
    data.write(x)

# with open("task5_00", "w") as data:
#     data.write(x)

# with open("task5_01", "w") as data:
#     data.write(x)