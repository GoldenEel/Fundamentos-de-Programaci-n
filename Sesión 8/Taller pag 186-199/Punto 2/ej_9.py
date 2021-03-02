# -*- coding: utf-8 -*-
"""
Un comercio dispone de dos tipos de artículos en fichas correspondientes a 
diversas sucursales con los siguientes campos:
• código del artículo A o B, 
• precio unitario del artículo, 
• número de artículos.
La última ficha del archivo de artículos tiene un código de artículo, 
una letra X. Se pide:
• el número de artículos existentes de cada categoría, 
• el importe total de los artículos de cada categoría.
"""
A = 0
B = 0
imp_A = 0
imp_B = 0
tot_compra = 0
cont_A = 0
cont_B = 0
n = int(input('Cantidad de articulos: '))
x = 0
while x < n: 
    x=x+1
    cod = input('Ingrese el código del articulo (A o B): ')
    if cod == 'A':
        if A <= 0:
            A = int(input('Ingrese el precio unitario de A: '))
        imp_A = imp_A +A
        cont_A = cont_A +1
        tot_compra = tot_compra + A
    if cod == 'B':
        if B <= 0:
            B = int(input('Ingrese el precio unitario de B: '))
        imp_B = imp_B +B
        cont_B = cont_A +1
        tot_compra = tot_compra + B
print(f'Total compra: {tot_compra}\nNumero de articulos A: {cont_A}\nNumero de articulos B: {cont_B}\nImporte articulos A: {imp_A}\nImporte articulos B: {imp_B}')
        
    