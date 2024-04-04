import matplotlib.pyplot as plt
import numpy as np
import random


def func(x):
    return np.exp(2*x)


def left_equipment():
    square = 0
    for i in range(len(xd) - 1):
        xi = [xd[i], xd[i], xd[i + 1], xd[i + 1]]
        yi = [0, func(xd[i]), func((xd[i])), 0]
        square += (func(xd[i]))*(1 / partition)
        ax.fill(xi, yi, facecolor='black', edgecolor='black', alpha=0.3)
    print(f'Сумма: {square}')


def right_equipment():
    square = 0
    for i in range(len(xd) - 1):
        xi = [xd[i], xd[i], xd[i + 1], xd[i + 1]]
        yi = [0, func(xd[i+1]), func((xd[i+1])), 0]
        square += (func(xd[i+1]))*(1 / (partition-1))
        ax.fill(xi, yi, facecolor='black', edgecolor='black', alpha=0.3)
    print(f'Сумма: {square}')


def centre_equipment():
    square = 0
    for i in range(len(xd) - 1):
        xi = [xd[i], xd[i], xd[i + 1], xd[i + 1]]
        yi = [0, func(xd[i]+((xd[i+1]-xd[i])/2)), func(xd[i]+((xd[i+1]-xd[i])/2)), 0]
        square += (func(xd[i]+(1/(2*partition))))*(1 / (partition-1))
        ax.fill(xi, yi, facecolor='black', edgecolor='black', alpha=0.3)
    print(f'Сумма: {square}')


def random_equipment():
    square = 0
    for i in range(len(xd) - 1):
        random_num = random.uniform(xd[i], xd[i + 1])
        xi = [xd[i], xd[i], xd[i + 1], xd[i + 1]]
        yi = [0, func(random_num), func(random_num), 0]
        square += (func(random_num))*(1 / (partition-1))
        ax.fill(xi, yi, facecolor='black', edgecolor='black', alpha=0.3)
    print(f'Сумма: {square}')


def trapezoid():
    square = 0
    for i in range(len(xd) - 1):
        random_num = random.uniform(xd[i], xd[i + 1])
        xi = [xd[i], xd[i], xd[i + 1], xd[i + 1]]
        yi = [0, func(xd[i]), func(xd[i+1]), 0]
        square += ((func(xd[i])+func(xd[i+1]))/2)*(1/(partition-1))
        ax.fill(xi, yi, facecolor='black', edgecolor='black', alpha=0.3)
    print(f'Сумма: {square}')


print("Введите желаемое число точек:")
points_num = int(input())
print("Введите желаемую мощность разбиения:")
partition = int(input())

while True:
    print("Выберите способ оснащения:")
    print("1 - левое оснащение\n2 - правое оснащение\n"
          "3 - центральное оснащение\n4 - случайное оснащение\n"
          "5 - трапеция\n")
    option = int(input())
    if option in [1, 2, 3, 4, 5]:
        break
    else:
        print("ERROR: введенная опция неподдерживается")


x = np.linspace(0, 1, points_num) #кортеж точек
xd = np.linspace(0, 1, partition) #кортеж разбиения
y = func(x)
fig, ax = plt.subplots()

if option == 1:
    left_equipment()
elif option == 2:
    right_equipment()
elif option == 3:
    centre_equipment()
elif option == 4:
    random_equipment()
elif option == 5:
    trapezoid()

plt.plot(x, y)
plt.title(f'Количество точек разбиения = {partition}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
