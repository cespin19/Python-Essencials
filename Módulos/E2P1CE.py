# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:46:44 2022

@author: cespin
"""

def espar():
    Datos_2021 = (1, 2, 3,4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302)
    par=[]
    impar=[]
    atip=[]
    for n in Datos_2021:
        if n%2==0:
            par.append(n)     
        else:
            impar.append(n)
        if n>100:
            atip.append(n)
    print(f"Elementos pares: {par}, elementos impares {impar}, elementos atipicos {atip}")