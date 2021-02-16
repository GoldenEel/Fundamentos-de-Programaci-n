# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 08:23:26 2021

@author: a
"""

print('Bienvenido a la calculadora')
n1 = float(input('Ingrese el primer número: '))
n2 = float(input('Ingrese el segundo número: '))
op = input('Ingrese el tipo de operación (+, -, /, *, **): ')
if op == '+':
    res = n1 + n2
    print(res)
elif op == '-':
    res = n1 - n2
    print(res)
elif op == '/':
    res = n1 / n2
    print(res)
elif op == '*':
    res =  n1 * n2
    print(res)
elif op == '**':
    res = n1 ** n2
    print(res)
else: 
    print('Porfavor especifique un operador valido')
    
