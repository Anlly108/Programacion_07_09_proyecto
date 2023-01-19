intentos = 0
while intentos<3:
    semilla = raw_input("Escriba la semilla de 4 digitos: ")
    digitos = len(semilla)
    if digitos>3:
        print("Cantidad de dígitos: ", digitos)
        numero_uno = int(semilla)
        for i in range(10):
            numero_dos = numero_uno*numero_uno
            snumero_dos = str(numero_dos)
            digitos_dos = len(snumero_dos)
            primerc = int((digitos_dos - digitos) / 2)
            snumero_tres = snumero_dos[primerc:primerc+digitos]
            print ("{}.  {}".format(i,snumero3))
            numero1 = int(snumero3)
    else:    
        emilla = int(semilla)
            intentos = intentos+
raise TypeError ("Semilla incorrecto ingresado en 3 intentos")
