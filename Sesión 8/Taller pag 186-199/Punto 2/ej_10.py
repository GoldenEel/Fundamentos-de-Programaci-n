# -*- coding: utf-8 -*-
"""
Una estación climatica proporciona un par de temperaturas diarias 
(máxima, miníma) (no es posible que alguna o ambas temperaturas sean 9
grados) La pareja fin de temperaturas es 0,0. Se pide determinar
el número de días cuyas temperaturas se han proporcionado, las medias 
máxima y mínima, el número de errores (temperaturas de 9) y el porcentaje 
que representaban.
"""
num_errores = 0
porc_errores = 0
num_dias = 0
x = True
med_max = 0
med_min = 0
prom_max= 0
prom_min = 0
while x == True:
    temp_min = int(input('Ingrese la temperatura máxima del día: '))
    temp_max = int(input('Ingrese la temperatura miníma del día: '))
    num_dias = num_dias + 1
    if temp_min == 0 and temp_max == 0:
        x = False
    if temp_min > temp_max:
        num_errores = num_errores + 1
    if temp_min == 9 or temp_max == 9:
        num_errores = num_errores + 1
    else:
        med_max = med_max + temp_max
        med_min = med_min + temp_min
prom_max = med_max / num_dias
prom_min = med_min / num_dias
porc_errores = (num_errores / num_dias) * 100
print(f'Cantidad de días: {num_dias}\nMedia temp max : {prom_max: .2f} Media temp min : {prom_min: .2f}')
print(f'Cantidad de errores: {num_errores} Porcentaje de temperaturas errores: {porc_errores: .1f}%')
        