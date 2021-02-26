# -*- coding: utf-8 -*-
"""
Calcular el factorial de un número n con metodos diferentes al del
ej_1
"""
num = int(input('Ingrese el número: '))
factorial = 1
i = 1
while i < num:
    i=i+1
    factorial= factorial*i
print(f'El factorial de {num} es {factorial}')