from PIL import Image
from random import *
from claseImagen import *
from numpy import *
import numpy as np
import operator as op
from operator import *

def comparacionEuclidiana(imagenDada,imagenMeta):
    sumatoria=0
    arregloDada = np.array(imagenDada)
    arregloMeta = np.array(imagenMeta)
    arregloNuevo = arregloMeta - arregloDada
    for fila in arregloNuevo:
        for columna in fila:
            sumatoria+= pow(columna,2)
    cantPixeles = (len(arregloDada)*len(arregloDada[0]))
    return sqrt(sumatoria)/cantPixeles

def establecerIndicesSimilitud(generacion,imagenMeta):
    tmp=0
    while(tmp<len(generacion)):
        generacion[tmp].indiceSimilitud = (comparacionEuclidiana(generacion[tmp].imagenGenerada,imagenMeta))
        tmp+=1
    nuevaLista = sorted(generacion, key=lambda imagen: imagen.indiceSimilitud)

    for i in nuevaLista:
        print(i.indiceSimilitud)
    return nuevaLista



