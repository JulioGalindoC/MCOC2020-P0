# MCOC2020-P0

# Mi computador
* Marca/modelo: MacBook Pro (15-inch, Mid 2010)
* Tipo: Notebook
* Año adquisición: 2010
* Procesador:
  * Marca/Modelo: Intel Core i7
  * Velocidad Base: 2.66 GHz
  * Número de núcleos: 2
  * Número de hilos: 4
  * Arquitectura: x86_64
* Tamaño de las cachés del procesador:
  * L2 Cache (por núcleo):	256 KB
  * L3 Cache:	4 MB
* Memoria:
  * Total: 8 GB
  * Tipo memoria: DDR3
  * Velocidad: 1067 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: NVIDIA GeForce GT 330M
  * Memoria dedicada: 1024 MB
  * Arquitectura: GT2xx
  * Resolución: 1440 x 900
* Disco 1: 
  * Marca: TOSHIBA MK5055GSXF
  * Tipo: HDD
  * Tamaño: 500 GB
  * Particiones: 1
  * Sistema de archivos: HFS+
* Dirección MAC de la tarjeta wifi: 60:33:4b:14:f6:70
* Dirección IP (Interna, del router): 192.168.86.22
* Dirección IP (Externa, del ISP): 190.215.226.26
* Proveedor internet: Gtd Manquehue S.A.
* Desempeño MATMUL:
  * Versión python: 3.7.5
  * Versión numpy: 1.19.1
* Desempeño MIMATMUL:  
  * Si bien las operaciones multiplicación y suma se realizan en tiempo constante (O(1)) es decir son operaciones rapidas, la función MIMATMUL tiene 3   ciclos for identados. Por lo tanto, el algoritmo tiene una complejidad O(n^3) convirtiendose de esta forma en un algoritmo lento.
  * La libreria scipy de la cual se importa la función MATMUL, esta programada principalmente en C++, un lenguaje de bajo nivel (se tiene más control de los usos de memoria), y el codigo esta compilado (de rapida ejecución). De esta forma, MATMUL es más rapido que MIMATMUL que esta programado en python que es un lenguaje de alto nivel e interpretado.
  * Si bien se puede ver que MATMUL exije más al procesador ocupa mucha menor memoria de esta forma no hay problemas de paginación o de segmaentación.
* Tamaño en memoria tipo de datos:
  * np.half: 26 bits
  * np.single: 28 bits
  * np.double: 32 bits
  * np.longdouble: 48 bits
* timing_inv_caso_1_half.py: TypeError: array type float16 is unsupported in linalg
* timing_inv_caso_1_longdouble.py: TypeError: array type float128 is unsupported in linalg
  
