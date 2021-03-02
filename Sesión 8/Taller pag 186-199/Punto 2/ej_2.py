# -*- coding: utf-8 -*-
"""
Dado el nombre de un mes y si el año es o no bisiesto, deducir
el numero de días del mes.
"""
print('Ingrese todos los valores en números.')
dia = int(input('Ingrese el día: '))
mes = int(input('Ingrese el mes: ').lstrip('0'))
ano = int(input('Ingrese el año: '))
err = 'Digito una fecha imposible.'
bisiesto = None
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    bisiesto = True
    print('El año es bisiesto')
else:
    bisiesto = False
    print('El año no es bisiesto')
    
if mes > 12 or dia > 31:
    print(err)
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes ==10 or mes == 12 and dia <= 31:
    print(f'Su fecha es {dia}/{mes}/{ano}')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia <= 30:
    print(f'Su fecha es {dia}/{mes}/{ano}')
elif mes == 2 and bisiesto == True and dia <= 29:
    print(f'Su fecha es {dia}/{mes}/{ano}')
elif mes == 2 and bisiesto == False and dia <= 28:
    print(f'Su fecha es {dia}/{mes}/{ano}')
else:
    print(err)
    
