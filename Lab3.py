import numpy as np
from PIL import Image


def rysuj_pasy_pionowe_szare(w, h, grub, kolor):
    size = (h, w)
    tab = np.zeros(size, dtype=np.uint8)
    tab[::] = 255

    for i in range(h):
        for j in range(0, w, grub*2):
            tab[i][j:j+grub] = kolor

    return Image.fromarray(tab)


def rysuj_ramki_szare(w,h,grub, kolor):
    size = (h, w)
    arr = np.full(size, kolor, dtype=np.uint8)
    shift = 0
    kolor_ramki = 255
    while shift < w / 2 or shift < h / 2:
        arr[(grub + shift):(h - grub - shift), (grub + shift):(w - grub - shift)] = kolor_ramki
        shift += grub
        if kolor_ramki == 255:
            kolor_ramki = kolor
        else: kolor_ramki = 255

    return Image.fromarray(arr)


def rysuj_ramki_kolorowe(w, kolor, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = kolor[0]
    kolor_g = kolor[1]
    kolor_b = kolor[2]
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r) % 256
        kolor_g = (kolor_g - zmiana_koloru_g) % 256
        kolor_b = (kolor_b - zmiana_koloru_b) % 256
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


def negatyw_L(obraz):
    tab = np.array(obraz)
    h, w = tab.shape

    for i in range(h):
        for j in range(w):
            tab[i][j] = 255 - tab[i][j]

    return Image.fromarray(tab)


def negatyw_RGB(obraz):
    tab = np.array(obraz)
    h, w = tab.shape[0:2]

    for i in range(h):
        for j in range(w):
            tab[i][j][0] = 255 - tab[i][j][0]
            tab[i][j][1] = 255 - tab[i][j][1]
            tab[i][j][2] = 255 - tab[i][j][2]

    return Image.fromarray(tab)


def negatyw(obraz):
    if obraz.mode == "1":
        return negatyw_1(obraz)
    elif obraz.mode == "L":
        return negatyw_L(obraz)
    elif obraz.mode == "RGB":
        return negatyw_RGB(obraz)
    return obraz


def rysuj_po_skosie_szare(w, h, a, b):  # formuła zmiany wartości elemntów tablicy a*i + b*j
    t = (h, w) # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)


"""
Kolor zmienia się w cyklu czerwony, zielony, niebieski
"""
def koloruj_w_paski(obraz, grub):
    if (obraz.mode != "1"):
        print("obraz musi być w trybie 1")
        return obraz

    tab = np.array(obraz, dtype=np.uint8)
    h, w = tab.shape
    print(h)
    print(w)
    size = (h, w, 3)
    new_tab = np.full(size, 255, dtype=np.uint8)

    kolor = 100
    ile = int(h / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if tab[i][j] == 0:
                    if k % 3 == 0:
                        new_tab[i, j] = [255, 0, 0]
                    elif k % 3 == 1:
                        new_tab[i, j] = [0, 255, 0]
                    else:
                        new_tab[i, j] = [0, 0, 255]

    return Image.fromarray(new_tab)


# obraz1 = rysuj_ramki_szare(200, 100, 9, 100)
obraz2 = rysuj_pasy_pionowe_szare(200, 100, 9, 50)
obraz2.show()
# obraz1.save("Zad1_ramki.png")
# obraz2.save("Zad1_pasy.png")

# Zad 2
gwiazdka = Image.open("gwiazdka.bmp")
obraz2 = negatyw(gwiazdka)
obraz2.save("gwiazdka_negatyw.png")

# obraz4 = rysuj_ramki_kolorowe(200, [20, 120,220], 6, 9, -6)
# obraz4.save("kolorowe_ramki.png")
# obraz4_neg = negatyw(obraz4)
# obraz4_neg.save("kolorowe_ramki_neg.png")

obraz1 = rysuj_po_skosie_szare(300, 100, 6, 9)
obraz1.save("skos_szare.png")
obraz2 = negatyw(obraz1)
obraz2.save("skos_szare_neg.png")




















