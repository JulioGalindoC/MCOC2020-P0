#                                                         #
#      Materia: Metodos Computacionales en IOC            #
#                                                         #
#      Entrega 2                                          #
#                                                         #
#      Alumno: Julio Andres Galindo Carazas               #
#                                                         #
#      Fecha: 07/08/2020                                  #
#                                                         #
###########################################################
#
# DESEMPEÑO FUNCION MATMUL (10 CORRIDAS)
#########################################

from scipy import matmul, rand
from time import perf_counter

N = [2, 5, 10,
     12, 15, 20,
     30, 40, 45,
     50, 55, 60,
     75, 100, 125,
     160, 200,250,
     350, 500,600,
     800,1000,2000,
     5000, 10000]

num_runs = 10 

for i in range(num_runs) :
    
    dts = []
    mem = []
    name =(f'matmul{i}.txt')
    fid = open(name, 'w')

    for i in N :
        
        A = rand(i,i)
        B = rand(i,i)

        t1 = perf_counter()
        C = A@B
        t2 = perf_counter()

        dt = t2 - t1

        size = 3 * (i**2) * 8
    
        dts.append(dt)
        mem.append(size)

        fid.write(f'{i} {dt} {size}\n')

        fid.flush()

    fid.close()
