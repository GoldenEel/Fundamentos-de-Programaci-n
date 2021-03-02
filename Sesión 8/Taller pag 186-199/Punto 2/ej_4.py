# -*- coding: utf-8 -*-
"""
Determinar la media de una lista de números positivos terminada con un
 número no positivo después del último número valido
"""
#No es lo mismo que el ej_1 ? No entiendo la diferencia.
#ej_1 :
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
media_lista = numpy.mean(n_list)
print(f'La media de la lista es {media_lista: .2f}')
