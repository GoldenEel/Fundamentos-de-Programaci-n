# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 08:38:31 2021

@author: a
"""

altura = float(input('Ingrese la altura del rectángulo: '))
base = float(input('Ingrese la base del rectángulo: '))
perim = altura * 2 + base * 2
area = base * altura
print(f'El perimetro del rectángulo es {perim} cm y su área es {area} cm^2')