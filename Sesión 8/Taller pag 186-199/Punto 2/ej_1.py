# -*- coding: utf-8 -*-
"""
Determinar la media de una lista indefinida de números positivos,
terminados con un número negativo. 
"""
import numpy
n_list = []
x = True
while x == True:
    num = int(input('Agrege un numero a la lista: '))
    if num >= 0:
        n_list.append(num)
        continue
    else: 
        break
mediana_lista = numpy.mean(n_list)
print(f'La mediana de la lista es {mediana_lista: .2f}')