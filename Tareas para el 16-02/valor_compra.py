# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:56:22 2021

@author: a
"""

compra = float(input('Ingrese el valor de su compra: '))
IVA = compra * 0.19
compra_descuento = compra * 0.95
valor_compra = compra_descuento + IVA
print(f'El valor final de su crompra es: {valor_compra: .2f} pesos')