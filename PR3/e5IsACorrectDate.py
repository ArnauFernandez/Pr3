"""
Matteo Vilchez, Arnau Fernández
7/11/2023
ASIXc1C M03 UF1 PR3
IsACorrectDate
Programa que comprovi si una data és correcte.
El programa ha de demanar una data, dia, mes i any (en el format DD/MM/AAAA).
Cal recordar que hi ha anys de traspàs.
NO es pot fer servir funcions de calendari com ara datetime de Python
"""
dia = input("Introduce el día: ")
mes = input("Introduce el mes: ")
any = input("Introduce el año: ")
if int(any) % 4 == 0 and (int(any) % 100 != 0 or int(any) % 400 == 0):
    print("es un año bisiesto")
if mes == "01" or mes == "03" or mes == "05" or mes == "07" or mes == "08" or mes == "10" or mes == "12" and int(dia) >0 and int(dia) <= 31:
    print("fecha correcta")
    if int(dia) > 31:
        print("Fecha incorrecta")
elif mes == "04" or mes == "06" or mes == "09" or mes == "11" and int(dia) >0 and int(dia) <= 30:
    print("fecha correcta")
    if int(dia) > 30:
        print("Fecha incorrecta")
elif mes == "02":
    if int(dia) > 28 or int(dia) == 29:
        print("Fecha correcta")
else:
    print("Fecha incorrecta")
