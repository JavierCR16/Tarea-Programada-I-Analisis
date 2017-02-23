from PIL import Image
from random import *

def createPopulation(cantidad, width, height):
    arrayPoblacion = []
    tmp = 0
    size = width, height
    while (tmp!=cantidad):
        child = Image.new("L", size, "white")
        for x in range(size[0]):
            for y in range(size[1]):
                if(choice([True,False])):
                    coordinates = x,y
                    child.putpixel(coordinates, randrange(0,255,1))
        arrayPoblacion.insert(tmp, child)
        tmp+=1
    return arrayPoblacion
