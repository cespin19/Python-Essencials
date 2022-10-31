# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:39:12 2022

@author: cespin
"""

import E1P1CE
import E1P2CE
import E2P1CE
import E2P2CE
import E3CE
while True:
    print ("*********Menú de Funciones***********")
    print ("1) Ejecutar programa de tipos de variables")
    print ("2) Ejecutar programa de tipos de variables ingresadas por teclado")
    print ("3) Ejecutar programa separador de pares e impares y valores atípicos")
    print ("4) Ejecutar programa de revisión de condiciones para contraseña")
    print ("5) Ejecutar programa de números menores y mayores en una lista")
    print ("6) Salir")
    op = int(input ("Ingrese la opción deseada: "))
    if op==1:
        E1P1CE.tipos()
    elif op==2:
        E1P2CE.tipoing()
    elif op==3:
        E2P1CE.espar()
    elif op==4:
        E2P2CE.contrarev()
    elif op==5:
        E3CE.evaluacion()
    elif op==6:
        break
    else:
        print ("Opción incorrecta ")