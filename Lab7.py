import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]


def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    w, h = inicjaly.size
    w1, h1 = obraz.size
    for i, j in zakres(w, h):
        if i + m < w1 and j + n < h1 and inicjaly.getpixel((i, j)) == 0:
            obraz.putpixel((i + m, j + n), kolor)
    return obraz


def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    inicjaly_pix = inicjaly.load()
    obraz_pix = obraz.load()
    w, h = inicjaly.size
    w1, h1 = obraz.size
    for i, j in zakres(w, h):
        if i + m < w1 and j + n < h1 and inicjaly_pix[i, j] == 0:
            obraz_pix[i + m, j + n] = kolor
    return obraz


def wstaw_inicjaly_maska(obraz, inicjaly, m, n):  # w miejscu m, n zmienia tylko te pixele, które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (255 - p[0], 255- p[1], 255 - p[2]))
    return obraz1


def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n):  # w miejscu m, n zmienia tylko te pixele, które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    obraz_pix = obraz.load()
    inicjaly_pix = inicjaly.load()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly_pix[i, j] == 0:
                p = obraz_pix[i + m, j + n]
                obraz_pix[i + m, j + n] = (255 - p[0], 255- p[1], 255 - p[2])
    return obraz


""" Zad 2a """
obraz = Image.open("beksinski.png")
inicjaly = Image.open("inicjaly.bmp")
obraz_copy = obraz.copy()

w1 = obraz.size[0] - inicjaly.size[0]
h1 = obraz.size[1] - inicjaly.size[1]
obraz1 = wstaw_inicjaly(obraz_copy, inicjaly, w1, h1, (255, 0, 0))
# obraz1.show()

""" Zad 2b"""
obraz_copy = obraz.copy()
w1 = int(w1 / 2)
h1 = int(h1 / 2)
obraz2 = wstaw_inicjaly_maska(obraz_copy, inicjaly, w1, h1)
# obraz2.show()


""" Zad 3a """
obraz_copy = obraz.copy()
w1 = obraz.size[0] - inicjaly.size[0]
h1 = obraz.size[1] - inicjaly.size[1]
obraz3 = wstaw_inicjaly_load(obraz_copy, inicjaly, w1, h1, (255, 0, 0))
# obraz3.show()

""" Zad 3b"""
obraz_copy = obraz.copy()
w1 = int(w1 / 2)
h1 = int(h1 / 2)
obraz4 = wstaw_inicjaly_maska_load(obraz_copy, inicjaly, w1, h1)
obraz4.show()




















