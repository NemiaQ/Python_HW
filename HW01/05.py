# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

a_x = int(input('Введите координаты первой точки (X): '))
a_y = int(input('Введите координаты первой точки (Y): '))
b_x = int(input('Введите координаты второй точки (X): '))
b_y = int(input('Введите координаты второй точки (Y): '))

result = round((((b_x - a_x) ** 2 + (b_y - a_y) ** 2) ** 0.5), 2)
print(f'Расстояние между точками составляет: {result}')
