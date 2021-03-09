# -*- coding: utf-8 -*-
"""
La suma de los primeros 100 números cuadrados
"""
suma = 0
cant_num = int(input('Digite la cantidad de números:  ')) +1
for x in range(cant_num):
    exp = x ** 2
    suma = suma + (exp)
    print(f'El cuadrado de {x} es {exp}\n La suma acumulada es {suma}')    
print(f'La suma final es {suma}')