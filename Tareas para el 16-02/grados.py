# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 08:34:58 2021

@author: a
"""

celsius = float(input('Ingrese una temperatura en grados celsius: '))
far = (celsius * (9/5)) + 32
kelv = celsius + 273.15
print(f'{celsius} grados celsuis son {far} grados farenheit y {kelv} grados kelvin.')
