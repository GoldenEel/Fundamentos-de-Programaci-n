# -*- coding: utf-8 -*-
"""
Se desea leer las calificaciones de una clase de informatica y contar el 
número total de aprobados
"""
num_est = int(input('Ingrese el número de estudiantes: '))
x = 1
rep = 0
apr = 0
while x <= num_est:
    x=x+1
    n1 = int(input('Ingrese la nota 1: '))
    n2 = int(input('Ingrese la nota 2: '))
    n3 = int(input('Ingrese la nota 3: '))
    n_final = (n1+n2+n3)/3
    if n_final <3:
       rep = rep+1
    else:
        apr = apr+1
print(f'{rep} estudiantes reprobaron, {apr} estudiantes aprobaron')