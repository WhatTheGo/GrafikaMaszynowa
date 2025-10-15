import numpy as np
from PIL import Image


def rysuj_pasy_pionowe_szare(w, h, grub, kolor):
    size = (h, w)
    tab = np.zeros(size, dtype=np.uint8)
    tab[::] = 255

    for i in range(w):
        for k in range(0, w, grub*2):
            for j in range(k, k+grub):
                tab[i][j] = kolor

    return Image.fromarray(tab)


def negatyw_1(obraz):
    tab = np.asarray(obraz, dtype=np.uint8)
    h, w = tab.shape

    for i in range(h):
        for j in range(w):
            tab[i][j] = abs(tab[i][j] - 1)

    return Image.fromarray(tab)


def negatyw(obraz):
    if obraz.mode == "1":
        return negatyw_1(obraz)
    return


obraz1 = Image.open("inicjaly.bmp")
obraz2 = negatyw(obraz1)
obraz2.show()

