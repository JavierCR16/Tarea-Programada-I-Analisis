from math import*
from decimal import Decimal
from PIL import Image
import numpy as np

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

x = Image.open("bn.png")
y = Image.open("7gen.png")
print(segunda(x,y))

#print (minkowski_distance([0,0,0],[255,255,255],1))

#print (minkowski_distance([255,255,255],[255,255,255],1))
