# -*- coding: utf-8 -*-
"""
Calcular factorial (otro metodo)
"""
n = int(input('Ingrese un número: '))
factorial = 1
x = 1
while x <= n:
    factorial = factorial * x
    x = x+1
print(f'El factorial de {n} es {factorial}')
