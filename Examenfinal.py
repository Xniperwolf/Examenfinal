import os
import time
import csv
import random
from funcionesexamen import *
os.system("cls")


#git init
#git commit -m
#git status
#git add *
#git add funciones.py etc...
#git push


trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez","Pedro Rodríguez","Laura Hernández", "Miguel Sanchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldosalazar = []

sueldorandom = random.randint(300000,2500000)
descsalud = 0.07*sueldorandom
descafp = 0.12*sueldorandom
sueldolíquido = sueldorandom-(descafp+descsalud)
dictrabajadores = []
descafplista = []
descsaludlista = []
sueldoliquidolista = []

while True:
    os.system("cls")
    print("Bienvenido a la aplicación de Sueldos")
    print("--------------------------------------")
    time.sleep(1)

    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de Sueldos")
    print("5. Salir del programa")

    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("ERROR! Ingrese una opción correcta!")
        except:
            print("Ingrese un número entero (opciones de 1 a 5)")
            os.system("cls")

    if opc == 1:
        sueldosrandom()
            

    elif opc == 2:
        clasificacion()

    elif opc == 3:
        estadisticas()

    elif opc == 4:
        exportarcsv()





    else:
        os.system("cls")
        print("Finalizando programa...")
        time.sleep(1)
        print("Desarrollado por Ignacio Gutierrez")
        time.sleep(1)
        print("RUT 19.729.060-9")
        time.sleep(2)
        break

