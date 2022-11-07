import random


def delta(x, y):
    if x == 0:
        return 0
    elif x*y == 1:
        return 1
    elif x != 0 and y == 0:
        return -1


'''X1 = [-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1]
X2 = [-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,1,1,1]'''
X1 = [0,0,0,0,1,1,0,0,1,0,0,0,1,1,1,1,0,1,1,0]
X2 = [0,0,0,0,1,0,0,0,0,1,0,1,1,1,0,1,0,1,1,1]
x0 = 1

'''#сигналы для биполярного нейрона
y1 = 1
y2 = -1'''

#сигналы для бинарного нейрона
y1 = 1
y2 = 0

#значения у1 и у2 после будем сравнивать с полученными результатами
y12 = []
y12.append(y1)
y12.append(y2)

#создаем список весов, обнуляем
weights = []
for i in range(21):
    weights.append(0)

#список входа нейрона изображение1 и х0 в начале списка
array_x1 = []
array_x1.append(x0)
for elem in X1:
    array_x1.append(elem)
print(f'X1 = {array_x1}')

#аналогично для изображение2
array_x2 = []
array_x2.append(x0)
for elem in X2:
    array_x2.append(elem)

y = y1
print(f'y = {y}')

#корректируем веса связей по правилу Хебба (по формуле)
for i in range(len(weights)):
    weights[i] += delta(array_x1[i], y)
print(f'w =  {weights}')

print(f'\nX2 = {array_x2}')
y = y2
print(f'y = {y}')

#корректируем веса связей по изображению2 (по формуле)
for i in range(len(weights)):
    weights[i] += delta(array_x2[i], y)

for i in range(len(weights)):
    weights[i] += array_x2[i] * y
print(f'w =  {weights}')
print('прогон букв окончен!\n\n')
print('\nПроверка качества обучения:')

#сумма весовых коэффициентов для изобр1
s1 = weights[0]
for i in range(1, len(array_x1)):
    s1 += array_x1[i] * weights[i]
print(f'S1 = {s1}', end =', ')

#выход нейрона:
y_1 = 1 if s1>0 else -1
print(f'выход нейрона для Х1 = {y_1}')

#сумма весовых коэффициентов для изобр2
s2 = weights[0]
for i in range(1, len(array_x2)):
    s2 += array_x2[i] * weights[i]
print(f'S2 = {s2}', end =', ')

#выход нейрона:
y_2 = 1 if s2>0 else 0
print(f'выход нейрона для Х2 = {y_2}')

#сравниваем полученные значения у_1, у_2 с начальными значениями (у1,у2)
yy = []
yy.append(y_1)
yy.append(y_2)

if yy == y12:
    print('\nGood job! Наши значения равны целевому вектору')