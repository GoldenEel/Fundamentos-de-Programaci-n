# -*- coding: utf-8 -*-
"""
Calcular el factorial de un número N utilizando la estructura desde
"""
n = int(input('Ingrese un valor: '))
factorial = 1
for x in range(n):
    factorial = factorial * (n-x)
print(f'El factorial de {n} es {factorial}')