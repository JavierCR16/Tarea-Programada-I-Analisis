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
            if(similitudPixel==0.0):
                aptos+=[[i,j]]
    return aptos

def establecerIndicesSimilitud(generacion,imagenMeta,modalidad):
    tmp=0
    while(tmp<len(generacion)):
        if(modalidad==0):
            print("Usar Euclideana")
            generacion[tmp].indiceSimilitud = comparacionEuclidiana(generacion[tmp].imagenGenerada, imagenMeta)
        elif(modalidad==1):
            print("Usar funcion nuestra")
        else:
            print("usar funcion de internet")
        tmp+=1
    nuevaLista = sorted(generacion, key=lambda imagen: imagen.indiceSimilitud)
    return nuevaLista

def indiceSimilitudPropia(imagenDada, imagenMeta):

    arregloImagen = np.array(imagenDada)
    anchoCuadrante= int(len(arregloImagen)/4)
    x=anchoCuadrante

    largoCuadrante= int(len(arregloImagen[0])/4)
    y=largoCuadrante

    matrizAuxiliar=[]
    filaMatriz =[]

    fila= 0
    columna=0

    arregloCuadrantes=[]

    while(len(arregloCuadrantes)!= 16):

        while(fila<largoCuadrante):

            matrizAuxiliar+= [arregloImagen[fila][columna:largoCuadrante].tolist()]
            fila+=1
        arregloCuadrantes.append(matrizAuxiliar)

        fila=largoCuadrante
        largoCuadrante+=y
        matrizAuxiliar=[]

        if(fila==len(arregloImagen)):
            columna=anchoCuadrante
            anchoCuadrante+= x
            fila =0
            largoCuadrante=y
    print("Cuadrantes hechos: "+ str(len(arregloCuadrantes)))
