import numpy as np
from PIL import Image

# Zadanie 5
def rysuj_pasy_pionowe_szare(w, h, grub, kolor):
    size = (h, w)
    tab = np.zeros(size, dtype=np.uint8)
    tab[::] = 255

    for i in range(h):
        for j in range(0, w, grub*2):
            tab[i][j:j+grub] = kolor

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


def rysuj_po_skosie_szare(w, h, a, b):  # formuła zmiany wartości elemntów tablicy a*i + b*j
    t = (h, w) # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)


def rgb_to_cmyk(rgb_array):
    # Przekształć wartości RGB na zakres [0, 1]
    rgb = rgb_array.astype(float) / 255
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]

    # Oblicz kanał Kk (black)
    k = 1 - np.max(rgb, axis=2)

    # Uniknij dzielenia przez zero
    c = (1 - r - k) / (1 - k + 1e-8)
    m = (1 - g - k) / (1 - k + 1e-8)
    y = (1 - b - k) / (1 - k + 1e-8)

    # Zastąp NaN (dla czystej czerni) zerami
    c[np.isnan(c)] = 0
    m[np.isnan(m)] = 0
    y[np.isnan(y)] = 0

    # Przekształć na zakres [0, 255]
    cmyk = np.stack((c, m, y, k), axis=2) * 255
    return cmyk.astype(np.uint8)


def roznica(arr1, arr2):
    h, w = arr1.shape
    arr3 = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            arr3[i][j] = abs(arr1[i][j] - arr2[i][j])

    return Image.fromarray(arr3)


kanal_r1 = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 10, 50), dtype=np.uint8)
kanal_g1 = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 18, 50), dtype=np.uint8)
kanal_b1 = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 26, 50), dtype=np.uint8)
obraz1 = rysuj_pasy_pionowe_kolorowe(kanal_r1, kanal_g1, kanal_b1)
obraz1.save("obraz6.png")

# Zad 6
# a = rysuj_po_skosie_szare(300, 200, 6, 9)
# a.show()
# a_ext = np.expand_dims(a, axis=-1)
# combined = np.concatenate((obraz1, a_ext), axis=-1)
# combined_image = Image.fromarray(combined)
# combined_image.save("obraz7.png")

# Zad 7
cmyk_array = rgb_to_cmyk(np.asarray(obraz1))
cmyk_obraz = Image.fromarray(cmyk_array, mode="CMYK")
cmyk_obraz.save("obraz8.tiff")

arr_c = cmyk_array[:, :, 0]
c_im = Image.fromarray(arr_c)
c_im.save("c.png")

arr_obraz1 = np.array(obraz1)
arr_r = arr_obraz1[:, :, 0]
r_im = Image.fromarray(arr_r)
r_im.save("r.png")

obraz_roznica = roznica(arr_c, arr_r)
obraz_roznica.save("roznica.png")


