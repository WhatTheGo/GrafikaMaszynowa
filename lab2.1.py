from pickletools import uint8

import numpy as np
from PIL import Image
from numpy.ma.core import asarray

obraz1 = Image.open("inicjaly.bmp")
print("tryb", obraz1.mode)
print("format", obraz1.format)
print("rozmiar", obraz1.size)

arr1 = np.asarray(obraz1)
print("typ danych tablicy", arr1.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy", arr1.shape)  # rozmiar tablicy - warto porównac z wymiarami obrazka


def rysuj_ramke_w_obrazie(obraz, grub):
    arr = np.asarray(obraz)
    arr = arr.astype(np.uint8)
    h, w = arr.shape

    if grub > h or grub > w:
        arr = arr.astype(bool)
        return Image.fromarray(arr)

    for i in range(h):
        for j in range(grub):
            arr[i][j] = 0
            arr[i][w-j-1] = 0

    for i in range(w):
        for j in range(grub):
            arr[j][i] = 0
            arr[h-j-1][i] = 0

    arr = arr.astype(bool)
    return Image.fromarray(arr)

obraz2 = rysuj_ramke_w_obrazie(obraz1, 2)
obraz2.show()