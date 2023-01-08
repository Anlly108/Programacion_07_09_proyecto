import time
def generarmatriz(filas, columnas):
    matriz = []    # La inicializamos vacia 

    valorinicial = 0   # El primer elemento empieza en 0

     # Por cada una de las filas de la matriz
    for i in range(1, filas + 1):       
        lista =   # Inicializamos la lista para el número de fila

         # Por cada una de las columnas de la matriz
        for j in range(1, columnas + 1):       

            if i % 2 == 0:     # Si es par 
                lista.append(valorinicial)      # Agregamos el siguiente valor a nuestra lista

            else:           # Si es impar
                lista.insert(0, valorinicial)   # Insertamos el siguiente valor al principio de la lista

            valorinicial += 1    # Actualizamos el contador para nuestro próximo elemento

        matriz.append(lista)      # Agregamos a nuestra matriz la lista temporal con los datos actuales

    return matriz    # Finalmente retornamos nuestra tabla

m,n=map(int,input("Ingrese número filas y columnas separados por espacios: ").split()) 
resultado=generarmatriz(m,n) 
for x in resultado: 
 print (x)
time.sleep(5)
