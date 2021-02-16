# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:28:39 2021

@author: a
"""

n = int(input('Numero de empleados: '))
k = float(input('Realizan una tarea en cuantas horas: '))
k1 = float(input('En cuantas horas desearia realizar la tarea: '))
n1 = (n*k)/k1
print(f'Para realizar la tarea en {k1} horas se necesitarian {n1} empleados')

