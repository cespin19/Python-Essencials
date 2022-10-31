# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 09:17:35 2022

@author: cespin
"""

def ls_cho(val):
    if val==1:
        wl=d1
    elif val==2:
        wl=d2
    elif val==3:
        wl=d3
    else:
        wl=d4
    return wl

def menu2():
    ct=True
    while ct:
        print ("Elija un diccionario para la demostración")
        print ("1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}")
        print ("2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}")
        print ("3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}")
        print ("4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}")
        opm2=int(input ("Ingrese la opción deseada: "))
        if opm2>=1 and opm2<=4:
            ct=False
        else:
            print ("Opción inválida, intente ingresar nuevamente")
    return opm2

def menu3(lis):
    ct=True
    while ct:
        naltos=int(input("Digite el número de valores altos que desea mostrar: "))
        nbajos=int(input("Digite el número de valores bajos que desea mostrar: "))
        if naltos<=len(lis) and nbajos<=len(lis) and naltos>0 and nbajos>0:
            break
        else:
            print ("El número de elementos ingresados no está dentro de las dimensiones de la lista, ingrese de nuevo")
    return naltos,nbajos


def encuentra(ls,al,ba):
    l2=[]
    for n in ls:
        l2.append(ls[n])
    l2.sort()
    lb=l2[:ba]
    la=l2[al*-1:]
    return la,lb

d1={"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}
d2={"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}
d3={"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
d4={"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}
ctr=True
while ctr:
    print ("Elija una opción:")
    print ("1) Demostración del cálculo de valores altos y bajos en diccionarios.")
    print ("2) Salir.")
    op=int(input ("Ingrese la opción elegida: "))
    if op==1:
        op2=menu2()
        lf=ls_cho(op2)
        na,nb=menu3(lf)
        la,lb=encuentra(lf,na,nb)
        ta=tuple(la)
        tb=tuple(lb)
        print(f"Valores calculados en formato lista: Lista valores altos= {la}, Lista de valores bajos= {lb}")
        print(f"Valores calculados en formato tupla: Tupla valores altos= {ta}, Tupla de valores bajos= {tb}")
    elif op==2:
        break
    else:
        print ("Opción ingresada es inválida")