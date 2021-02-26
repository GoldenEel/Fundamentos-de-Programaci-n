# -*- coding: utf-8 -*-
"""
Se desea leer de una consola una serie de números hasta obtener 
un número inferior a 100
"""
x=True
while x==True:
    num = int(input('Escriba un número: '))
    if num < 100:
        print('Escribio un número menor a 100')
        break
    