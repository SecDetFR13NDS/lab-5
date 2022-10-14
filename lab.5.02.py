a = float(input('Введіть число x1: '))
b = float(input('Введіть число x2: '))
c = float(input('Введіть число x3: '))
y = float(input('Введіть число Y: '))
if a % y == 0 and b % y == 0 and c % y == 0:
    print('Число У є дільником даних чисел')
else:
    print('Число У не є дільником даних чисел')
