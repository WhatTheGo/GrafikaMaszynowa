from pickletools import uint8

import numpy as np
from PIL import Image


# inicjaly = Image.open("inicjaly.bmp")
# print("tryb", inicjaly.mode)
# print("format", inicjaly.format)
# print("rozmiar", inicjaly.size)
#
# arr1 = np.asarray(inicjaly)
# print("typ danych tablicy", arr1.dtype)
# print("rozmiar tablicy", arr1.shape)


def rysuj_ramke_w_obrazie(obraz, grub):
    arr = np.asarray(obraz)
    arr = arr.astype(np.uint8)
    h, w = arr.shape

    arr[:h, :grub] = 0
    arr[:h, w-grub:w] = 0
    arr[:grub, :w] = 0
    arr[h-grub:h, :w] = 0
    arr = arr.astype(np.bool)
    return Image.fromarray(arr)


def rysuj_ramki(w,h,grub):
    size = (h, w)
    arr = np.zeros(size, dtype=np.uint8)
    shift = 0
    color = 1
    while shift < w / 2 or shift < h / 2:
        arr[(grub + shift):(h - grub - shift), (grub + shift):(w - grub - shift)] = color
        shift += grub
        if color == 0:
            color = 1
        else: color = 0

    arr = arr.astype(np.bool)
    return Image.fromarray(arr)


def rysuj_paski_pionowe(w,h,grub):
    size = (h, w)
    arr = np.ones(size, dtype=np.uint8)
    shift = 0

    while shift < w:
        arr[:h, shift:grub + shift] = 0
        shift += 2 * grub

    arr = arr.astype(np.bool)
    return Image.fromarray(arr)


"""
Obraz na wyjściu pokazuje czarne pionowe paski grubości grub zaczynając od lewej strony
każdy kolejny pasek ma wysokość zmniejszoną o połowę w stosunku do poprzedniego paska 
"""

def rysuj_wlasne(w,h, grub):
    size = (h, w)
    arr = np.ones(size, dtype=np.uint8)
    shift = 0
    i = 1

    while shift < w:
        arr[h - int(h / i):h, shift:grub + shift] = 0
        shift += 2 * grub
        i *= 2

    arr = arr.astype(np.bool)
    return Image.fromarray(arr)


def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_obraz_wstawiany = np.asarray(obraz_wstawiany).astype(np.int_)
    tab_obraz_bazowy = np.asarray(obraz_bazowy).astype(np.int_)
    h0, w0 = tab_obraz_wstawiany.shape
    h1, w1 = tab_obraz_bazowy.shape

    n_k = min(h1, n + h0)  # jesli wstawiany obraz wychodzi poza ramy nowego obrazu, to przycinamy
    m_k = min(w1, m + w0)  # jesli wstawiany obraz wychodzi poza ramy nowego obrazu, to przycinamy
    n_p = max(0, n)  # jesli miejsce wstawienia jest ujemne(wychodzi poza nowy obraz w górę), to przycinamy
    m_p = max(0, m)  # jesli miejsce wstawienia jest ujemne(wychodzi poza nowy obraz w lewo), to przycinamy
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_obraz_bazowy[i][j] = tab_obraz_wstawiany[i - n][j - m]
    tab = tab_obraz_bazowy.astype(bool)  # zapisanie tablicy w typie bool (obrazy czarnobiałe)
    return Image.fromarray(tab)

# obraz1 = rysuj_wlasne(105, 200, 10)
# obraz1.show()
# obraz1.save("Zad6.png")

obraz1 = Image.open("Zad2.png")
arr1 = np.asarray(obraz1, dtype=np.uint8)
print("tryb:", obraz1.mode)
print("wartość piksela (66,13):", obraz1.getpixel((66,13)))
print("wartość elementu tablicy (97,20):", arr1[97,20])

