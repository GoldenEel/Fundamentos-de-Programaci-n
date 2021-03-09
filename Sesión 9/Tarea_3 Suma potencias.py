# -*- coding: utf-8 -*-
"""
Imprimir las 30 primeras potencias de 10, sumar las potencias calculadas
"""
suma_potencias = 0
for x in range(31):
    if x > 0:
        exp = 10 ** x
        suma_potencias = suma_potencias + exp
        print(exp)
print(f'Suma total: {suma_potencias}')
