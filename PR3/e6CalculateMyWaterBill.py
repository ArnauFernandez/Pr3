"""
Matteo Vilchez, Arnau Fernández
7/11/2023
ASIXc1C M03 UF1 PR3
CalculateMyWaterBill
El preu que pagues per l’aigua que consumeixes. El consum es divideix en 5 trams de preus progressius.
El consum es calcula segons els m3 consumits. Qui més estalvi d’aigua fa, menys trams consumeix i,
per tant, més estalvia. Aquest sistema ajuda a fomentar un consum responsable.
Preu = (5.0 * 0.5849) + 6.40
"""
tipoVivienda = input("Introduce la letra (en Mayusculas) del habitatge:").upper()
consumo = float(input("Introduce el numero de m³ gastados:"))
TIPO_A = 2.46
TIPO_B = 6.40
TIPO_C = 7.25
TIPO_D = 11.21
TIPO_E = 12.10
TIPO_F = 17.28
TIPO_G = 28.01
TIPO_H = 40.50
TIPO_I = 61.31
tramo1 = 0.5849
tramo2 = 1.1699
tramo3 = 1.7548
tramo4 = 2.3397
tramo5 = 2.9246
precio=0
if consumo > 0 and consumo <=6 :
    if tipoVivienda == TIPO_A :
        precio= (consumo * tramo1) + TIPO_A
    elif tipoVivienda == TIPO_B:
        precio= (consumo * tramo1) + TIPO_B
    elif tipoVivienda == TIPO_C:
        precio= (consumo * tramo1) + TIPO_C
    elif tipoVivienda == TIPO_D:
        precio= (consumo * tramo1) + TIPO_D
    elif tipoVivienda == TIPO_E:
        precio= (consumo * tramo1) + TIPO_E
    elif tipoVivienda == TIPO_F:
        precio= (consumo * tramo1) + TIPO_F
    elif tipoVivienda == TIPO_G:
        precio= (consumo * tramo1) + TIPO_G
    elif tipoVivienda == TIPO_H:
        precio= (consumo * tramo1) + TIPO_H
    elif tipoVivienda == TIPO_I:
        precio= (consumo * tramo1) + TIPO_I
print("Tu factura de agua asciende a :",precio)
if consumo > 7 and consumo <= 9 :
    if tipoVivienda == TIPO_A:
        precio = (consumo * tramo2) + TIPO_A
elif tipoVivienda == TIPO_B:
    precio = (consumo * tramo2) + TIPO_B
elif tipoVivienda == TIPO_C:
    precio = (consumo * tramo2) + TIPO_C
elif tipoVivienda == TIPO_D:
    precio = (consumo * tramo2) + TIPO_D
elif tipoVivienda == TIPO_E:
    precio = (consumo * tramo2) + TIPO_E
elif tipoVivienda == TIPO_F:
    precio = (consumo * tramo2) + TIPO_F
elif tipoVivienda == TIPO_G:
    precio = (consumo * tramo2) + TIPO_G
elif tipoVivienda == TIPO_H:
    precio = (consumo * tramo2) + TIPO_H
elif tipoVivienda == TIPO_I:
    precio = (consumo * tramo2) + TIPO_I
print("Tu factura de agua asciende a :", precio)
if consumo > 10 and consumo <= 15 :
    if tipoVivienda == TIPO_A :
        precio = (consumo * tramo3) + TIPO_A
    elif tipoVivienda == TIPO_B:
        precio = (consumo * tramo3) + TIPO_B
    elif tipoVivienda == TIPO_C:
        precio = (consumo * tramo3) + TIPO_C
    elif tipoVivienda == TIPO_D:
        precio = (consumo * tramo3) + TIPO_D
    elif tipoVivienda == TIPO_E:
        precio = (consumo * tramo3) + TIPO_E
    elif tipoVivienda == TIPO_F:
        precio = (consumo * tramo3) + TIPO_F
    elif tipoVivienda == TIPO_G:
        precio = (consumo * tramo3) + TIPO_G
    elif tipoVivienda == TIPO_H:
        precio = (consumo * tramo3) + TIPO_H
    elif tipoVivienda == TIPO_I:
        precio = (consumo * tramo3) + TIPO_I
print("Tu factura de agua asciende a :",precio)
if consumo > 16 and  consumo <= 18:
    if tipoVivienda == TIPO_A:
        precio = (consumo * tramo4) + TIPO_A
    elif tipoVivienda == TIPO_B:
        precio = (consumo * tramo4) + TIPO_B
    elif tipoVivienda == TIPO_C:
        precio = (consumo * tramo4) + TIPO_C
    elif tipoVivienda == TIPO_D:
        precio = (consumo * tramo4) + TIPO_D
    elif tipoVivienda == TIPO_E:
        precio = (consumo * tramo4) + TIPO_E
    elif tipoVivienda == TIPO_F:
        precio = (consumo * tramo4) + TIPO_F
    elif tipoVivienda == TIPO_G:
        precio = (consumo * tramo4) + TIPO_G
    elif tipoVivienda == TIPO_H:
        precio = (consumo * tramo4) + TIPO_H
    elif tipoVivienda == TIPO_I:
        precio = (consumo * tramo4) + TIPO_I
print("Tu factura de agua asciende a :",precio)
if consumo >=18:
    if tipoVivienda == TIPO_A:
        precio = (consumo * tramo5) + TIPO_A
    elif tipoVivienda == TIPO_B:
         precio = (consumo * tramo5) + TIPO_B
    elif tipoVivienda == TIPO_C:
            precio = (consumo * tramo5) + TIPO_C
    elif tipoVivienda == TIPO_D:
            precio = (consumo * tramo5) + TIPO_D
    elif tipoVivienda == TIPO_E:
            precio = (consumo * tramo5) + TIPO_E
    elif tipoVivienda == TIPO_F:
            precio = (consumo * tramo5) + TIPO_F
    elif tipoVivienda == TIPO_G:
            precio = (consumo * tramo5) + TIPO_G
    elif tipoVivienda == TIPO_H:
            precio = (consumo * tramo5) + TIPO_H
    elif tipoVivienda == TIPO_I:
            precio = (consumo * tramo5) + TIPO_I
print("Tu factura de agua asciende a :",precio)


