# -*- coding: utf-8 -*-
"""
Calcular el valor máximo de una serie de 100 números
pero lo hice de 10 para no digitar 100 números
"""
n = 1
num = int(input('Digite un número'))
maximo = num
while n <10 :
    n = n+1
    num = int(input('Digite un número'))
    if num > maximo:
        maximo=num
print(f'El número máximo es {maximo}')