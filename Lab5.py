from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe
    print()

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


def zlicz_piksele(obraz, kolor):
    ile = 0
    kolor = np.array(kolor)
    arr = np.array(obraz, dtype=np.uint8)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if (arr[i][j] == kolor).all():
                ile += 1
    return ile


""" Zad 1a """
im1 = Image.open("Sebastian_Adamus.png")
print("Statystyki obrazu Sebastian_Adamus.png (im1):")
statystyki(im1)
r, g, b = im1.split()
# rysuj_histogram_RGB(im, "obraz")
# rysuj_histogram_L(r, "kanał r")
# rysuj_histogram_L(g, "kanał g")
# rysuj_histogram_L(b, "kanał b")

""" Zad 1b """
print("kanał r:", zlicz_piksele(r, 155))
print("kanał g:", zlicz_piksele(g, 155))
print("kanał b:", zlicz_piksele(b, 155))

""" Zad 1c """
print("Ilość pikseli [155,155,155] w im1:", zlicz_piksele(im1, [155,155,155]))

""" Zad 2a """
im2 = Image.open("Sebastian_Adamus.jpg")
print("\nStatystyki obrazu Sebastian_Adamus.jpg (im2):")
statystyki(im2)

""" Zad 2b """
diff1 = ImageChops.difference(im1, im2)
print("\nStatystyki różnicy Sebastian_Adamus.png (im1) i Sebastian_Adamus.jpg (im2):")
statystyki(diff1)
diff1.show()

""" Zad 2c """
im3 = Image.open("Sebastian_Adamus2.jpg")
diff2 = ImageChops.difference(im1, im3)
print("\nStatystyki różnicy Sebastian_Adamus.png (im1) i Sebastian_Adamus2.jpg (im3):")
statystyki(diff2)
diff2.show()










