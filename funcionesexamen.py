import os
import time
import csv
import random

os.system("cls")


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
trabajadorcompleto = []

def sueldosrandom():
        os.system("cls")
        print("Asignar sueldos aleatorios")
        print("----------------------------")
        time.sleep(2)
        print("Cargando...")
        time.sleep(3)
        os.system("cls")
        print("Sueldos Asignados, se mostará por inicial de Nombre en orden de lista: ")
        print("-----------------------------------------------------------------------------")
        time.sleep(2)
        sueldorandom = random.randint(300000,2500000)
        for x in trabajadores:
            sueldorandom = random.randint(300000,2500000)
            sueldosalazar.append(sueldorandom)
            descsalud = 0.07*sueldorandom
            descafp = 0.12*sueldorandom
            sueldolíquido = sueldorandom-(descafp+descsalud)
            print(f"Trabajador: {x[0:15]}\n", "Sueldo Base: ", "$", sueldorandom, "DESCAFP: $", descafp, "DESCSALUD: $",descsalud, "Líquido: $",round(sueldolíquido))
            print("               ")

            time.sleep(1)
            trabajadorcompleto = {"Trabajador":[trabajadores], "Bruto":sueldosalazar, "DescSalud":descsalud, "DescAFP":descafp, "Liquido":sueldolíquido}
            dictrabajadores.append(trabajadorcompleto)
            descsaludlista.append(descsalud)
            descafplista.append(descafp)
            sueldoliquidolista.append(sueldolíquido)

def clasificacion():
        os.system("cls")
        if not sueldorandom or not sueldosalazar:
            print("No hay sueldos asignados, ocupe la opción 1 primero.")
            time.sleep(2)
        else:
            print("Sistema de clasificación de sueldos: ")
            time.sleep(2)
            print("Sueldos menores a 800000")
            print("---------------------------")
            sueldosalazar.sort()
            for x in trabajadores:
                    print("Sueldos de menor a mayor (3000000 hasta 2500000)")
                    print(f"Trabajador: {x[0]}\n", "Sueldo: ", "$", sueldosalazar[0])
                    time.sleep(2)
                    break
            
def estadisticas():
        os.system("cls")
        print("Estadísticas de sueldos: ")
        print("---------------------------")
        time.sleep(2)
        sueldosalazar.sort()
        for x in sueldosalazar:
            print("Sueldo más alto es $: ", sueldosalazar[9])
            time.sleep(3)
            print("Sueldo más bajo: ", "$", sueldosalazar[0])
            time.sleep(3)
            promediosueldos = sum(sueldosalazar)/9
            print("Promedio de sueldos es: ", promediosueldos)
            time.sleep(3)
            break

def exportarcsv():
        os.system("cls")
        with open("archivosueldos.csv","w",newline="") as archivo:
            secciones = ["Trabajador","Bruto","DescSalud","DescAFP","Liquido"]
            escritor = csv.DictWriter(archivo, fieldnames=secciones)
            escritor.writeheader()
            escritor.writerow(trabajadorcompleto)

            print("Archivo creado exitosamente!")
            time.sleep(2)