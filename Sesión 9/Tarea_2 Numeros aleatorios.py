# -*- coding: utf-8 -*-
"""
Escribir un programa que genere aleatoriamente 100 datos y sume todos los números,
los negativos, los positivos y calcule el promedio de todos los números, de los positivos
y los negativos ademas calcule el mayor y em menor de los positivos y los 
negativos
"""
from numpy import random
mayor_pos = float('-inf')
min_pos = float('inf')
mayor_neg = float('-inf')
min_neg = 0
num_pos = 0
num_neg = 0
promedio = 0
sum_pos = 0
sum_neg = 0
prom_pos = 0
Cant_num = int(input('Cantidad de números aleatorios: '))
for x in range(Cant_num):
    rand_num = random.randint(-100, 100)
    print('Número: ',rand_num)
    if rand_num >0:
        num_pos = num_pos +1
        sum_pos = sum_pos + rand_num
        if rand_num > mayor_pos:
            mayor_pos = rand_num 
        if rand_num < min_pos:
            min_pos = rand_num
    if rand_num < 0:
        num_neg = num_neg +1
        sum_neg = sum_neg + rand_num
        if rand_num > mayor_neg:
            mayor_neg = rand_num
        if rand_num < min_neg:
            min_neg = rand_num
prom_neg = sum_neg / num_neg
prom_pos = sum_pos / num_pos
promedio = (sum_pos + sum_neg)/ Cant_num
print(f'\n\nPromedio {promedio: .0f}\nPromedio negativos {prom_neg: .0f}\nPromedio positivos {prom_pos: .0f}')
print(f'Máximo positivo {mayor_pos}\nMáximo negativo {mayor_neg}\nMinimo positivo {min_pos}\nMinimo negativo {min_neg}')
print(f'Suma negativos {sum_neg}\nSuma positivos {sum_pos}\nCantidad negativos {num_neg}\nCantidad positivos {num_pos}')