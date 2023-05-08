import csv
import sys
from ClaseViajero import viajero
lista = []
with open ('infoViajeros.csv') as archi:
    reader = csv.reader(archi, delimiter=';')
    for fila in reader:
        ##print(f"numero viajero: {fila[0]}, dni: {fila[1]}, nombre: {fila[2]},apellido: {fila[3]},millas acumuladas: {fila[4]}")
        nuevoObjeto = viajero (int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]))
        lista.append(nuevoObjeto)
    num = int(input("\n INGRESAR NUMERO DE VIAJERO: "))
    for k in range (len(lista)):
        if lista[k].numero() == num:
            buscado = lista [k] 
            print("Se ha encontrado al viajero ")
            print("1: Consultar cantidad de millas ")
            print("2: Acumular millas ")
            print("3: Canjear Millas")
            print("0: salir")
            opcion = int(input("\n INGRESAR NUMERO DE OPCION: "))
            if opcion == 1: 
                print (f"\n La cantidad de millas acumuladas es : {buscado.cantidadTotalMillas()}")
            elif opcion == 2:
                acum = int(input("\n Ingresar cantidad de millas a acumular: "))
                print(f"\n ahora el total de millas acumulado es: {buscado.acumularmillas(acum)} millas")
            elif opcion == 3:
                masmillas = int(input("\n Ingresar cantidad de millas a canjear: "))
                ##buscado.canjearMillas(masmillas)
                print(f" \n usted a canjeado: {masmillas} ahora la cantidad de millas que tiene es: {buscado.canjearMillas(masmillas)}")
            elif opcion == 0:
                exit()
    k=0
    while k < len(lista):
        ##print(f"\n El objeto de el viajero {lista[k].numero()} llamado {lista[k].nombree()} ocupa {sys.getsizeof(lista[k])} bytes de memoria")
        k+=1