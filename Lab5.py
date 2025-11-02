import random
from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def statystyki(image):
    s = stat.Stat(image)
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


def negatyw_RGB(obraz):
    tab = np.array(obraz)
    h, w = tab.shape[0:2]

    for i in range(h):
        for j in range(w):
            tab[i][j][0] = 255 - tab[i][j][0]
            tab[i][j][1] = 255 - tab[i][j][1]
            tab[i][j][2] = 255 - tab[i][j][2]

    return Image.fromarray(tab)


def mieszaj_kanaly(obraz):
    r, g, b = obraz.split()
    n_obraz = negatyw_RGB(obraz)
    nr, ng, nb = n_obraz.split()
    arr1 = [r, g, b, nr, ng, nb]
    arr2 = []
    for i in range(3):
        j = random.randrange(5)
        arr2.append(arr1[j])

    return Image.merge("RGB", (arr2[0], arr2[1], arr2[2]))


def czy_equal(obraz1, obraz2):
    w1, h1 = obraz1.size[0:2]
    w2, h2 = obraz2.size[0:2]

    if h1 != h2:
        return False
    if w1 != w2:
        return False

    arr1 = np.array(obraz1, dtype=np.uint8)
    arr2 = np.array(obraz2, dtype=np.uint8)
    for i in range(h1):
        for j in range(w1):
            if arr1[i][j] != arr2[i][j]:
                return False

    return True


def rozpoznaj_mix(obraz, mix):
    r, g, b = obraz.split()
    n_obraz = negatyw_RGB(obraz)
    nr, ng, nb = n_obraz.split()
    mix_r, mix_g, mix_b = mix.split()
    arr1 = [r, g, b, nr, ng, nb]
    arr1_s = ["r", "g", "b", "nr", "ng", "nb"]
    arr2 = [mix_r, mix_g, mix_b]
    arr3 = []
    for i in range(3):
        for j in range(6):
            if czy_equal(arr2[i], arr1[j]):
                arr3.append(arr1_s[j])

    if len(arr3) != 3:
        return "Złe obrazy"

    return f'r -> {arr3[0]}, g -> {arr3[1]}, b -> {arr3[2]}'


""" Zad 1a """
im = Image.open("Sebastian_Adamus.png")
print("Statystyki obrazu Sebastian_Adamus.png (im):")
statystyki(im)
r, g, b = im.split()
# rysuj_histogram_RGB(im, "obraz")
# rysuj_histogram_L(r, "kanał r")
# rysuj_histogram_L(g, "kanał g")
# rysuj_histogram_L(b, "kanał b")


""" Zad 1b """
# print("kanał r:", zlicz_piksele(r, 155))
# print("kanał g:", zlicz_piksele(g, 155))
# print("kanał b:", zlicz_piksele(b, 155))

""" Zad 1c """
print("Ilość pikseli [155,155,155] w im:", zlicz_piksele(im, [155, 155, 155]))


""" Zad 2a """
im2 = Image.open("Sebastian_Adamus.jpg")
print("\nStatystyki obrazu Sebastian_Adamus.jpg (im2):")
statystyki(im2)

""" Zad 2b """
diff1 = ImageChops.difference(im, im2)
print("\nStatystyki różnicy Sebastian_Adamus.png (im) i Sebastian_Adamus.jpg (im2):")
statystyki(diff1)

""" Zad 2c """
im3 = Image.open("Sebastian_Adamus2.jpg")
diff2 = ImageChops.difference(im, im3)
print("\nStatystyki różnicy Sebastian_Adamus.png (im) i Sebastian_Adamus2.jpg (im3):")
statystyki(diff2)


""" Zad 3a """
t = np.array(im, dtype=np.uint8)
t_r = t[:, :, 0]
t_g = t[:, :, 1]
t_b = t[:, :, 2]
im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)

""" Zad 3b """
im1 = Image.merge("RGB", (im_r, im_g, im_b))

""" Zad 3c """
plt.figure(figsize=(16, 16))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.title("im")
plt.imshow(im)
plt.axis('off')
plt.subplot(2,2,2)
plt.title("im1")
plt.imshow(im1)
plt.axis('off')
plt.subplot(2,2,3)
plt.title("Wynik porównania")
plt.imshow(ImageChops.difference(im, im1))
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.25)
plt.savefig('fig1.png')
plt.show()

""" Zad 3d """
# Nie widać różnicy pomiędzy obrazami


""" Zad 4a """
mix = mieszaj_kanaly(im)
mix.save("mix.png")

""" Zad 4b """
print(rozpoznaj_mix(im, mix))


""" Zad 5 """
