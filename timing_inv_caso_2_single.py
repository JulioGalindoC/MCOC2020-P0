#                                                         #
#      Materia: Metodos Computacionales en IOC            #
#                                                         #
#      Entrega 4                                          #
#                                                         #
#      Alumno: Julio Andres Galindo Carazas               #
#                                                         #
#      Fecha: 12/08/2020                                  #
#                                                         #
###########################################################
from scipy import rand, linalg
from numpy import zeros, single
from time import perf_counter

def matriz_laplaciana(N, dtype = single) :
    A = zeros((N,N), dtype = dtype)
    for i in range(N) :
        for j in range(N) :
            if i == j :
                A[i,j] = 2
            if i + 1 == j :
                A[i,j] = -1
            if i - 1 == j :
                A[i,j] = -1
    return A

#
# DESEMPEÑO scipy.linalg.inv - overwrite_a=False - np.half
############################################################

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
    name =(f'scipy_linalg_single{i}.txt')
    fid = open(name, 'w')
    
    for i in N :
        
        A = matriz_laplaciana(i)
        
        t1 = perf_counter()
        
        A_inv = linalg.inv(A)
        
        t2 = perf_counter()
        
        dt = t2 - t1
        
        size = 2 * (i**2) * 28   # 2 Matrices, i^2, 28 bits por cada numero float
        
        dts.append(dt)
        mem.append(size)
        
        fid.write(f'{i} {dt} {size}\n')
        
        fid.flush()
    
    fid.close()
