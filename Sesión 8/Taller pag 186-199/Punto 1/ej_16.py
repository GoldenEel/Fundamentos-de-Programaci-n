# -*- coding: utf-8 -*-
"""
Se dispone de un cierto número de valores de los cuales el último es el 999
y se desea determinar el valor máximo de las medias correspondientes a 
parejas de valores sucesivos.
"""
n1 = int(input('Ingrese el número 1: '))
n2 = int(input('Ingrese el número 2: '))
Max = (n1 + n2)/2
while n1 < 999 and n2 < 999:
    n1 = int(input('Ingrese el número 1: '))
    n2 = int(input('Ingrese el número 2: '))
    M = (n1 + n2)/2
    if M > Max:
        Max = M
print('La media maxima es ', Max)
