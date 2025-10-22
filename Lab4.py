import numpy as np
from PIL import Image

# Zadanie 6
def rysuj_pasy_pionowe_szare(w, h, grub, kolor):
    size = (h, w)
    tab = np.zeros(size, dtype=np.uint8)
    tab[::] = 255

    for i in range(0, w, grub*2):
        for j in range(h):
            tab[j][i:i+grub] = kolor

    return Image.fromarray(tab)


def rysuj_pasy_pionowe_kolorowe(kanal_r, kanal_g, kanal_b):
    h = kanal_r.shape[0]
    w = kanal_r.shape[1]
    size = (h, w, 3)
    tab = np.zeros(size, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i][j] = [kanal_r[i][j], kanal_g[i][j], kanal_b[i][j]]

    return Image.fromarray(tab)


kanal_r1 = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 10, 50), dtype=np.uint8)
kanal_g1 = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 18, 50), dtype=np.uint8)
kanal_b1 = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 26, 50), dtype=np.uint8)
obraz1 = rysuj_pasy_pionowe_kolorowe(kanal_r1, kanal_g1, kanal_b1)
obraz1.show()















