# -*- coding: utf-8 -*-
"""
La suma de los primeros 100 números cuadrados
"""
suma = 0
for x in range(101):
    suma = suma + (x**2)
print(suma)