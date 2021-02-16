# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:08:39 2021

@author: a
"""
import math

r = float(input('Ingrese el radio del circulo: '))
A = (r**2) * math.pi
L = 2*math.pi*r
print(f"El area del circulo es {A} y la longitud de su circumferencia es {L}")