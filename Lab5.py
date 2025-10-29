from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


im = Image.open("beksinski.png")

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

def rysuj_histogram_RGB(obraz, title):
    hist = obraz.histogram()
    plt.title(title)
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()

def rysuj_histogram_L(obraz, title):
    hist = obraz.histogram()
    plt.title(title)
    plt.bar(range(256), hist[:])
    plt.show()


""" Zad 1 """
statystyki(im)
r, g, b = im.split()
# rysuj_histogram_RGB(im, "obraz")
# rysuj_histogram_L(r, "kanał r")
# rysuj_histogram_L(g, "kanał g")
# rysuj_histogram_L(b, "kanał b")

























