# Задача 2. Напишите программу, которая принимает на
# вход координаты двух точек и находит расстояние между
# ними в 2D пространстве.
import math


def pifagor(coordinate_a, coordinate_b):
    result = math.sqrt((coordinate_a[0] - coordinate_b[0]) ** 2 + (coordinate_a[1] - coordinate_b[1]) ** 2)
    return round(result, 3)


point1 = [int(i) for i in input("Введите точки х и у для точки А: ").split()]
point2 = [int(i) for i in input("Введите точки х и у для точки B: ").split()]

print(f'Расстояние между точками с координатами А = {point1} и B = {point2} равно {pifagor(point1, point2)}')
