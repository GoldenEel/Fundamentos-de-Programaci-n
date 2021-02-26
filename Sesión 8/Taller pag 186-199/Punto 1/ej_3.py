# -*- coding: utf-8 -*-
"""
Calcular la sumas de los n primeros números enteros
Ej: n=3 seria 1+2+3 = 6
"""
n = int(input('Ingrese la cantidad de números: '))
suma = 0
res_suma = 0
for x in range(n):
    suma = suma+1
    res_suma = res_suma + suma
print(res_suma)
    
