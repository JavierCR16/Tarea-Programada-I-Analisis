from PIL import Image
from random import choice

def createPopulation(cantidad, width, height):
    arrayPoblacion = []
    tmp = 0
    widthTmp=0
    heightTmp=0
    size = width, height
    while (tmp!=cantidad):
        child = Image.new("1", size, "white")
        for x in range(size[0]):
            for y in range(size[1]):
                if(choice([True,False])):
                    coordinates = x,y
                    child.putpixel(coordinates, 0)
        arrayPoblacion.insert(tmp, child)
        tmp+=1
    return arrayPoblacion
