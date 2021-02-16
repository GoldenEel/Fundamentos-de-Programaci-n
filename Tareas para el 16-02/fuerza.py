# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 08:28:57 2021

@author: a
"""
#No estoy seguro si las formula es correcta para este ejercicio
m = float(input('Ingrese la masa del objeto (kg): '))
us = float(input('Ingresse el coeficiente de rozamiento estático del objeto: '))
fuerza = m * us
print(f'La fuerza necesaria para mover este objeto es {fuerza}N')