# -*- coding: utf-8 -*-
"""
Escribir un algoritmo que permita escribir en una pantalla la frase 
'Desea continuar? S/N' hasta que la respuesta sea S o N 
"""
x = True
while x == True:
    print('Desea continuar? S/N')
    respuesta = input('Respuesta: ')
    if respuesta == 'S' or respuesta == 'N':
        break 