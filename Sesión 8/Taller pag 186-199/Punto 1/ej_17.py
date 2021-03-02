# -*- coding: utf-8 -*-
"""
Detección de entradas numéricas - enteros- erróneas
"""
SW = 0 
while SW == 0:
    N = input('Ingrese un valor: ')
    if N.isnumeric() == False:
        print('Dato no valido')
        print('Ejecute nuevamente')
        SW = 1
    else:
        print(f'Correcto {N} es entero')