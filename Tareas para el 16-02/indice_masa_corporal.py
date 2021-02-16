# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:14:23 2021

@author: a
"""

peso =  float(input('Ingrese su peso en kg: '))
estatura = float(input('Ingrese su estatura en metros: '))
BMI = peso / (estatura**2)
print(f'Su indice de masa corporal es {BMI}')
