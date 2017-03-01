from PIL import Image
from random import *
from claseImagen import *
from numpy import *
from funcionesAdaptavilidad import *
import numpy as np
import random

def createPopulation(cantidad, width, height, imagenMeta):
    arrayPoblacion = []
    tmp = 0
    size = width, height
    imagenMeta = imagenMeta.convert('L')
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
    return arrayPoblacion

def mutacion(imagenMutar, porcentajeMutacion, imagenMeta):
    imagenMutar = np.array(imagenMutar.imagenGenerada)
    imagenMeta = np.array(imagenMeta)
    contadorMutaciones = 0
    pixelesACambiar= (porcentajeMutacion/100)*(len(imagenMutar)*len(imagenMutar[0]))
    while (contadorMutaciones < pixelesACambiar):
        fila = random.randrange(0, len(imagenMutar))
        columna = random.randrange(0, len(imagenMutar[fila]))
        if(random.choice([True,False])):
            if(imagenMeta[fila][columna]==imagenMutar[fila][columna]):
                pass
            elif((imagenMeta[fila][columna] < imagenMutar[fila][columna])):
                dif = imagenMutar[fila][columna] - imagenMeta[fila][columna]
                imagenMutar[fila][columna] = abs(imagenMutar[fila][columna] - random.randrange(0, dif))
            else:
                dif = imagenMutar[fila][columna]
                imagenMutar[fila][columna] = imagenMutar[fila][columna] + random.randrange(0, 255-dif)
        contadorMutaciones += 1
    imagenMutar = Image.fromarray(imagenMutar)
    return imagenMutar

def cruzar(generacion, porcentaje):
    tmp = generacion
    nuevoArray=[]
    poblacion = len(generacion)
    #Cruzar los dos mas aptos
    #
    hijo1, hijo2 = cruzarAux(tmp[0], tmp[1])
    tmp=tmp[2:]
    imagen1 = imagen()
    imagen2 = imagen()
    imagen1.imagenGenerada = hijo1
    imagen2.imagenGenerada = hijo2
    nuevoArray.append(imagen1)
    nuevoArray.append(imagen2)
    #
    while(len(nuevoArray) < poblacion):
        hijo1=hijo2=0
        while(hijo1==hijo2):
            hijo1 = randrange(0,len(tmp))
            hijo2 = randrange(0,len(tmp))
        hijo1=tmp[hijo1]
        hijo2=tmp[hijo2]
        tmp.remove(hijo1)
        tmp.remove(hijo2)
        if(randrange(0,100)<=porcentaje):
            x,y=cruzarAux(hijo1, hijo2)
            imagen1 = imagen()
            imagen2 = imagen()
            imagen1.imagenGenerada=x
            imagen2.imagenGenerada=y
            nuevoArray.append(imagen1)
            nuevoArray.append(imagen2)
        else:
            nuevoArray.append(hijo1)
            nuevoArray.append(hijo2)
    return nuevoArray

def cruzarAux(hijo1, hijo2):
    nodo1 = np.array(hijo1.imagenGenerada)
    nodo2 = np.array(hijo2.imagenGenerada)
    for fila in range(0, len(nodo1)):
        for columna in range(0,len(nodo1[0])):
            if(random.choice([True,False])):
                tmp=nodo1[fila][columna]
                nodo1[fila][columna]=nodo2[fila][columna]
                nodo2[fila][columna]=tmp
    hijo1 = Image.fromarray(nodo1)
    hijo2 = Image.fromarray(nodo2)
    return (hijo1, hijo2)







