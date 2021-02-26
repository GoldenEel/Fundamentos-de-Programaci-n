# -*- coding: utf-8 -*-
"""
Lee sucesivamente números del tecado hasta que aparezca un número 
comprendido entre 1 y 5
"""
x=True
while x == True:
    num = int(input('Ingrese un número: '))
    if num <= 5 and num >= 1:
        print('Ingreso un número entre 1 y 5')
        break
