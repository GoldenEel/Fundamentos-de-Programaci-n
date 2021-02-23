# -*- coding: utf-8 -*-
print('Sistema de notas de un curso de programación')
num_est = int(input('Cuantos estudiantes: '))
est_rep = 0
est_gan = 0
grup_ac = 0
est_gan_ac = 0
est_rep_ac = 0
est_rep_prom = 0
est_gan_prom = 0
nota_min = 5
nota_max = 0
x = 1
for x in range(num_est):
    x = x+1
    nom_est = input('Ingrese el nombre del estudiante: ')
    n1= float(input('Ingrese la nota 1: '))
    n2= float(input('Ingrese la nota 2: '))
    n3= float(input('Ingrese la nota 3: '))
    n_def = (n1+n2+n3) / 3
    grup_ac = grup_ac + n_def
    #Nota maxima y minima
    if n_def >= nota_max:
        nota_max = n_def
    if n_def <= nota_min:
        nota_min = n_def    
    #Notas ganadas/perdidas
    if n_def >= 3:
        est_gan = est_gan + 1
        est_gan_ac = est_gan_ac + n_def
        est_gan_prom = est_gan_ac / est_gan
        print(f'Aprobo, la definitiva de {nom_est} es {n_def: .2f}')
    else:
        est_rep = est_rep + 1
        est_rep_ac = est_rep_ac + n_def
        est_rep_prom = est_rep_ac / est_rep

        print(f'Reprobo, su definitiva es {n_def: .2f}') 
grup_prom = grup_ac / num_est
#Print de todos los puntos
print('Otros calculos: ')
print(f'El promedio del grupo fue {grup_prom: .2f} la nota máxima fue {nota_max: .2f} la minima fue {nota_min: .2f}\n{est_rep} estudiantes reprobaron, el promedio fue {est_rep_prom: .2f} \n{est_gan} estudiantes aprobaron, el promedio fue {est_gan_prom: .2f}')
