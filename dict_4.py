# задача 4

a = input('Введите коэффициент a: ')
b = input('Введите коэффициент b: ')
c = input('Введите коэффициент c: ')
a = float(a)
b = float(b)
c = float(c)
discriminant = b**2 - 4*a*c
if discriminant < 0:
    print('Корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('корень 1: ' + str(x1))
    print('корень 2: ' + str(x2))