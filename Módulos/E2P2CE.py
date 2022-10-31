# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 21:57:40 2022

@author: cespin
"""
def contrarev():
    print ("*******************Creación de contraseña********************")
    print ("Para ser válida, la contraseña debe cumplir con lo siguiente:")
    print ("-Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.")
    print ("-Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.")
    print ("-Debe contener al menos un número entre 0 y 9.")
    print ("-Debe contener un símbolo especial entre: $,%,*,@")
    print ("-Tamaño mínimo de 5 caracteres y máximo de 15.")
    cont=input("Ingrese la contraseña:")
    un=False
    dos=False
    tres=False
    cua=False
    if len(cont)>=5 and len(cont)<=15:
        for n in cont:
            for m in ("abcdefghij"):
                if m in n:
                    un=True
            for m in ("KLMNOPQRST"):
                if m in n:
                    dos=True
            for m in ("0123456789"):
                if m in n:
                    tres=True
            for m in ("$%*@"):
                if m in n:
                    cua=True
    if un==True and dos==True and tres==True and cua==True:
        print("Contraseña válida")
    else:
        print("Contraseña inválida")