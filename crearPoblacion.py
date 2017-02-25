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






