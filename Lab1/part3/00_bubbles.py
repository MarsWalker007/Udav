#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)
sd.circle(center_position=point, radius = radius)
# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код
def bubble(point, step, color):
    radius = 20
    for _ in range(3):
        radius += step
        colore = color
        sd.circle(center_position=point, radius=radius,color = colore )

point = sd.get_point(100, 300)
bubble(point=point, step=15, color='blue')

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for x in range(50, 1000, 100):
    point = sd.get_point(x, 450)
    bubble(point=point, step=1, color='white')
# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
for y in range(150, 300, 50):
    for x in range(250, 5000, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=1, color='white')
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=1, color='white')
# TODO здесь ваш код

sd.pause()
