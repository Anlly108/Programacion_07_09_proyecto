import time
m = int(input("Ingrese el numero M que representa la cantidad de terminos de la serie: "))
pi = 0  # Valor inicial del 
signo = 1  # Variable para alternar el signo cambiante
for i in range(1, m+1, 2):
    pi += (signo/i)
    signo = -1   # Alternar el signo cada vez
pi = round(pi, 10)
print("El valor de pi es "+str(pi))
time.sleep(5)