# -*- coding: utf-8 -*-
"""
Diseñar el algoritmo para imprimir la suma de los números impares menores 
o iguales que n
"""
n = int(input('Ingrese un número: '))
x= 0
while x <= n:
    x = x+1
    if x%2 != 0:
        print(x)