import numpy as np
from PIL import Image


def rysuj_pasy_pionowe_szare(w, h, grub, kolor):
    size = (h, w)
    tab = np.zeros(size, dtype=np.uint8)
    tab[::] = 255

    for i in range(0, w, grub*2):
        for j in range(h):
            tab[j][i:i+grub] = kolor

    return Image.fromarray(tab)


def negatyw_1(obraz):
    tab = np.array(obraz)
    h, w = tab.shape

    for i in range(h):
        for j in range(w):
            if tab[i][j] == 1:
                tab[i][j] = 0
            else:
                tab[i][j] = 1

    return Image.fromarray(tab)


def negatyw(obraz):
    if obraz.mode == "1":
        return negatyw_1(obraz)
    return


obraz1 = Image.open("inicjaly.bmp")
obraz2 = negatyw(obraz1)
obraz1.show()
obraz2.show()

# obraz1 = rysuj_pasy_pionowe_szare(200, 100, 10, 100)
# obraz1.show()



























