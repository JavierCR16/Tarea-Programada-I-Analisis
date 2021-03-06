from PIL import Image
from random import *
from claseImagen import *
from numpy import *
import numpy as np
from decimal import Decimal
from operator import *

def comparacionEuclidiana(imagenDada,imagenMeta):
    array1 = imagenDada.getdata()
    array2 = imagenMeta.getdata()
    size = width, height=imagenDada.size
    return sqrt(sum(pow(a - b, 2) for a, b in zip(array1, array2))) / (width*height)

def establecerIndicesSimilitud(generacion,imagenMeta, opcion):
    tmp=0
    while(tmp<len(generacion)):
        if(opcion==0):
            generacion[tmp].indiceSimilitud = comparacionEuclidiana(generacion[tmp].imagenGenerada, imagenMeta)
        elif(opcion==1):
            generacion[tmp].indiceSimilitud = segunda(generacion[tmp].imagenGenerada, imagenMeta)
        else:
            cuadrantesMeta = cuadrantes(imagenMeta)
            generacion[tmp].indiceSimilitud = indiceSimilitudPropia(generacion[tmp].imagenGenerada, cuadrantesMeta)
        tmp+=1
    nuevaLista = sorted(generacion, key=lambda imagen: imagen.indiceSimilitud)
    if(opcion ==2):
        nuevaLista= nuevaLista[::-1] #invierte la lista para que elmás apto quede de primero( FUNCION PROPIA )

    return nuevaLista



def compararCuadrantes(dada, meta):
    resultado = 0
    dif = 0
    for i in range(0,len(dada)):
        for j in range(0, len(dada[0])):
            if(meta[i][j]>dada[i][j]):
                dif = meta[i][j]-dada[i][j]
            else:
                dif = dada[i][j] - meta[i][j]
            resultado += 100-((dif*100)/255)
    return int(resultado/(len(dada)*len(dada[0])))

def indiceSimilitudPropia(imagenDada, cuadranteMeta):
    cuadranteDada = cuadrantes(imagenDada)
    resultado = 0
    for i in range(0,16):
        resultado += compararCuadrantes(cuadranteDada[i], cuadranteMeta[i])
    return float(resultado/16)

def cuadrantes(imagen):
    arregloImagen = np.array(imagen)
    anchoCuadrante = int(len(arregloImagen) / 4)
    x = anchoCuadrante
    largoCuadrante = int(len(arregloImagen[0]) / 4)
    y = largoCuadrante
    matrizAuxiliar = []
    filaMatriz = []
    fila = 0
    columna = 0
    arregloCuadrantes = []
    while (len(arregloCuadrantes) != 16):
        while (fila < anchoCuadrante):
            matrizAuxiliar += [arregloImagen[fila][columna:largoCuadrante].tolist()]
            fila += 1
        arregloCuadrantes.append(matrizAuxiliar)
        fila = anchoCuadrante
        anchoCuadrante += x
        matrizAuxiliar = []
        if (fila == len(arregloImagen)):
            columna = largoCuadrante
            largoCuadrante += y
            fila = 0
            anchoCuadrante = x
    return arregloCuadrantes

#Comparación por minkowski
def square_rooted(x):
    return round(sqrt(sum([a * a for a in x])), 3)

def nth_root(value, n_root):
    root_value = 1 / float(n_root)
    return round(value ** root_value, 3)#round(Decimal(value) ** Decimal(root_value), 3)


def minkowski_distance(x, y, p_value):
    result = nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)
    result = (result * 50) / 276
    return result

def segunda(x, y):
    size = width, height = x.size
    x = np.array(x.convert("RGB"), dtype='int64')
    y = np.array(y.convert("RGB"), dtype='int64')
    result = 0
    for i in range(0, len(x)):
        for j in range(0, len(x[0])):
            result += minkowski_distance(x[i][j], y[i][j], 1)
    result = result / (width * height)
    result = float(result * 50) / 105.833333333
    return int(result)