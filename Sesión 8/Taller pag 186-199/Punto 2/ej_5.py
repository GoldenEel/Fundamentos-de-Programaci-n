# -*- coding: utf-8 -*-
"""
Imprimir todos los números primos entre 2 y 1000
"""
for x in range(1000):
    prim = 0
    for i in range(2, x):
        if(x % i == 0):
            prim = prim+1
            break
    if prim==0 and x != 1 and x != 0:
        print(x)