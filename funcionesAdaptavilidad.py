from PIL import Image
from random import *
from claseImagen import *
from numpy import *
import numpy as np
import operator as op
from operator import *

def comparacionEuclidiana(imagenDada,imagenMeta):
    array1 = imagenDada.getdata()
    array2 = imagenMeta.getdata()
    size = width, height=imagenDada.size
    return sqrt(sum(pow(a - b, 2) for a, b in zip(array1, array2))) / (width*height)

def comparar(imagenDada, imagenMeta):
    aptos = []
    size = width, height = imagenMeta.size
    for i in range(0, width, 1):
        for j in range(0, height, 1):
            coordinates = i, j
            comparacion = abs(imagenDada.getpixel(coordinates)-imagenMeta.getpixel(coordinates))
            similitudPixel=(comparacion*50)//127.5
            if(similitudPixel<=10.0):
                aptos+=[[i,j]]
    return aptos

def establecerIndicesSimilitud(generacion,imagenMeta):
    tmp=0
    while(tmp<len(generacion)):
        generacion[tmp].indiceSimilitud = comparacionEuclidiana(generacion[tmp].imagenGenerada, imagenMeta)
        generacion[tmp].pixelesAptos = comparar(generacion[tmp].imagenGenerada, imagenMeta)
        tmp+=1
    nuevaLista = sorted(generacion, key=lambda imagen: imagen.indiceSimilitud)
    return nuevaLista



