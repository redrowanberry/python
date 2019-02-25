a = int(input())
m = a%10
a = a//10
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
print(m)

a = input("Input a: ")
b = input("Input b: ")
a,b = b,a
print(a + b)

import math

print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

discr = b ** 2 - 4 * a * c;
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
