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
#  Implementación Multiplicación de Matrices
###############################################

def mimatmul(A,B) :
    global C
    for i in range(len(A)) :
        for j in range(len(B[0])) :
            for k in range(len(B)) :
                C[i][j] += A[i][k] * B[k][j]
    return C
