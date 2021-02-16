# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 08:42:14 2021

@author: a
"""

horas_trabajadas = int(input('Ingrese el total de horas trabajadas: '))
horas_sueldo = int(input('Ingrese su sueldo por hora: '))
sueldo = horas_trabajadas *  horas_sueldo
if sueldo < 300:
    sueldo_total = (sueldo - (sueldo * 0.29022)) + (sueldo * 0.02)
else:
    sueldo_total = sueldo - (sueldo * 0.29022)

print(f'Su sueldo final es de {sueldo_total} dolares')