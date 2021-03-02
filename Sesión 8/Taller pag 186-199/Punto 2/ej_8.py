# -*- coding: utf-8 -*-
"""
Leer 10 números. Determinar la media de los números positivos
y la de los números negativos.
"""
pos_cont = 0
neg_cont = 0
pos = 0
neg = 0
pos_media = 0 
neg_media = 0
for x in range(10):
    n=int(input('Ingrese un número: '))
    if n<0:
        neg_cont= 1+ neg_cont
        neg = neg + n
    else:
        pos_cont = 1 + pos_cont
        pos = pos + n
pos_media = pos /pos_cont
neg_media = neg/neg_cont
print(f'La media de los números positivos es {pos_media}\nLa media de los números negativos es {neg_media}')