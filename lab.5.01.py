import math
x = float(input('Задайте Х: '))
if x >= -0.7:
    y = -6*math.pow(x, 2)+math.sin(x)
elif -9.9 < x < -0.7:
    y = math.log(math.fabs(x+math.sin(x)), math.e)
else:
    y = 12+math.fabs(math.sin(2*x))
print('Відповідь: ', y)
