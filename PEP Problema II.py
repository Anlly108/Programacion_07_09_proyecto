#Definir los valores de entrada
h = float(input("Indica la profundidad del pozo (en metros): ")) #Altura del pozo en metros
ld = float(input("Indica la distancia que el caracol asciende durante el día (en metros): ")) #Distancia diurna de ascenso en metros
ln = float(input("Indica la distancia que el caracol desciende durante la noche (en metros): ")) #Distancia nocturna ('resbalón') en metros

#Calcular el número de días para que el caracol salga del pozo
diasSalidaPozo = round((h) / (ld - ln)) #Número de días hasta que el caracol salga del pozo
        
print("El caracol sale del pozo en", diasSalidaPozo, "días")