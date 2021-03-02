# -*- coding: utf-8 -*-
"""
Leer notas de una clase y deducir todas aquellas que son notables
"""
num_est = int(input('Ingrese el número de estudiantes: '))
x = 1
notable = 0
while x <= num_est:
    x=x+1
    n1 = int(input('Ingrese la nota 1: '))
    n2 = int(input('Ingrese la nota 2: '))
    n3 = int(input('Ingrese la nota 3: '))
    n_final = (n1+n2+n3)/3
    if n_final >=3.5 and n_final < 4.5 :
       notable = notable+1
print(f'De {num_est} notas {notable} son notables (>=3,5 y < 4,5)')

