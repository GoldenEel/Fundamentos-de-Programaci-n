# -*- coding: utf-8 -*-
"""
Se tienen 3 calificaciones de alumnos, diseñar un algoritmo que calcule la 
nota de estudiantes de informatica. 
"""
print('Ingrese *** como nombre para terminar de calcular las notas')
nombre = 0
while nombre != "***":
    nombre = input('Ingrese el nombre del estudiante: ')
    n1 = int(input('Ingrese la nota de BASIC: '))
    n2 = int(input('Ingrese la nota de Pascal: '))
    n3 = int(input('Ingrese la nota de FORTRAN: '))
    media = (n1+n2+n3)/3
    print(f'La nota de {nombre} fue {media: .2f}')