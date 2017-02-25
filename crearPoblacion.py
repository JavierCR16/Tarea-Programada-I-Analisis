from PIL import Image
from random import *
from claseImagen import *
from numpy import *
import numpy as np
import operator as op
from operator import *
import random


#  **POSIBILIDAD PARA MUTAR**

    #img = Image.open(imagenDada).convert("L")
    #arr = np.array(imagenMeta)
    #tmp=0


    # for caca in arr:
    #    print(caca)
   # while(tmp<len(arr[0])): cambiar color
   #     arr[1][tmp]=0
    #    tmp+=1

    #imagen= Image.fromarray(arr) #Regresar a imagen
    #imagen.save("cambiadaOriginal.png")
def createPopulation(cantidad, width, height):#imagenMeta):
    arrayPoblacion = []
    tmp = 0
    size = width, height
   # imagenMeta= imagenMeta.convert('L')
    while (tmp!=cantidad):
        child = imagen()
        child.imagenGenerada = Image.new("L", size, "white")
        for x in range(size[0]):
            for y in range(size[1]):
                if(choice([True,False])):
                    coordinates = x,y
                    child.imagenGenerada.putpixel(coordinates, randrange(0,255,1))
        arrayPoblacion.insert(tmp, child)
        tmp+=1
        #arrayPoblacion[0].imagenGenerada.save("bn.png")

   # arrayPoblacion = establecerIndicesSimilitud(arrayPoblacion,imagenMeta)
   # for pene in arrayPoblacion:
    #    print(pene.indiceSimilitud)

    return arrayPoblacion

def mutacion(imagenMutar,porcentajeMutacion):
    imagenMutar = np.array(imagenMutar)

    contadorMutaciones = 0
    pixelesACambiar= (porcentajeMutacion/100)*cantidadPixeles(imagenMutar)

    #imagenMutar= Image.fromarray(imagenMutar)
   # imagenMutar.save("before.png")
    #imagenMutar = np.array(imagenMutar)

    while (contadorMutaciones < pixelesACambiar):
        fila = random.randrange(0, len(imagenMutar))
        columna = random.randrange(0, len(imagenMutar[fila]))
        imagenMutar[fila][columna] = random.randrange(0, 256)
        contadorMutaciones += 1
    imagenMutar = Image.fromarray(imagenMutar)
    #imagenMutar.save("nueva.png")

    return imagenMutar

    # while(porcentajeMutacion<seMutara):
    #    seMutara = random.randrange(0,101)


    #if(seMutara<= porcentajeMutacion):



def  cantidadPixeles(matriz):
    tmp = 0
    for fila in matriz:
        for columna in fila:
            tmp += 1


    return tmp

def cruzar(generacion, porcentaje):
    tmp = generacion
    nuevoArray=[]
    poblacion = len(generacion)
    while(len(nuevoArray) < poblacion):
        hijo1=hijo2=0
        while(hijo1==hijo2):
            hijo1 = randrange(0,len(tmp))
            hijo2 = randrange(0,len(tmp))
        hijo1=tmp[hijo1]
        hijo2=tmp[hijo2]
        tmp.remove(hijo1)
        tmp.remove(hijo2)
        hijo1=hijo1.imagenGenerada
        hijo2=hijo2.imagenGenerada
        if(randrange(0,100)<=porcentaje):
            hijo1,hijo2=cruzarAux(hijo1, hijo2)
        imagen1 = imagen()
        imagen2 = imagen()
        imagen1.imagenGenerada=hijo1
        imagen2.imagenGenerada=hijo2
        nuevoArray.append(imagen1)
        nuevoArray.append(imagen2)
    return nuevoArray

def cruzarAux(hijo1, hijo2):
    nodo1 = np.array(hijo1)
    nodo2 = np.array(hijo2)
    for fila in range(0, len(nodo1)):
        for columna in range(0,len(nodo1[0])):
            if(random.choice([True,False])):
                tmp=nodo1[fila][columna]
                nodo1[fila][columna]=nodo2[fila][columna]
                nodo2[fila][columna]=tmp
    hijo1 = Image.fromarray(nodo1)
    hijo2 = Image.fromarray(nodo2)
    return (hijo1, hijo2)







