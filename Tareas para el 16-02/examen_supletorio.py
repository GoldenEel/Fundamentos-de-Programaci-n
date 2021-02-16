# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:18:08 2021

@author: a
"""

p_sem = float(input('Ingrese la nota de su primer bimestre: '))
s_sem = float(input('Ingrese la nota de su segundo bimestre: '))
exm_spl =  10.5 - (p_sem + s_sem)
if exm_spl >5:
    print('Ya no puede ganar el semestre sin importar la nota en el examen supletorio')
else: 
    print(f'Para ganar el semestre necesita al menos un {exm_spl:.2f} en el examen supletorio')