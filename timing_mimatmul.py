#                                                         #
#      Materia: Metodos Computacionales en IOC            #
#                                                         #
#      Entrega 3                                          #
#                                                         #
#      Alumno: Julio Andres Galindo Carazas               #
#                                                         #
#      Fecha: 10/08/2020                                  #
#                                                         #
###########################################################
#
# Implementacion MIMATMUL
#########################################
from scipy import rand
from mimatmul import mimatmul
from time import perf_counter

N = [2, 5, 10,
     12, 15, 20,
     30, 40, 45,
     50, 55, 60,
     75, 100, 125,
     160, 200,250,
     350, 500]

num_runs = 10

for i in range(num_runs) :
    
    dts = []
    mem = []
    name =(f'matmul{i}.txt')
    fid = open(name, 'w')
    
    for i in N :
        
        A = rand(i,i)
        B = rand(i,i)
        
        s = (i,i)
        global C
        C = zeros(s)
        
        t1 = perf_counter()
        mimatmul(A,B)
        t2 = perf_counter()
        
        dt = t2 - t1
        
        size = 3 * (i**2) * 8
        
        dts.append(dt)
        mem.append(size)
        
        fid.write(f'{i} {dt} {size}\n')
        
        fid.flush()
    
    fid.close()
