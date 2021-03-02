# -*- coding: utf-8 -*-
"""
Determinar simultaneamente los valores máximo y mínimo de una lista
de 100 números (en este caso 10).
"""
num = int(input('Ingrese el número:  '))
maximo = num 
minimo = num
for x in range(9):
    num = int(input('Ingrese el número:  '))
    if num > maximo:
        maximo = num
    elif num < minimo:
        minimo = num
print(f'El número mayor ingresado fue {maximo} y el menor fue {minimo}')
