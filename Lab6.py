from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

def ocen_czy_identyczne(obraz1, obraz2):
    if obraz1.mode != obraz2.mode:
        return "obrazy nie są identyczne, bo obrazy mają różne tryby"
    if obraz1.size != obraz2.size:
        return "obrazy nie są identyczne, bo obrazy mają różny rozmiar"

    arr1 = np.array(obraz1, dtype=np.uint8)
    arr2 = np.array(obraz2, dtype=np.uint8)

    for i in range(arr1.shape[0]):
        for j in range(arr1.shape[1]):
            if (arr1[i][j] != arr2[i][j]).all():
                return "obrazy nie są identyczne, bo obrazy mają różne wartości pikseli"

    return "obrazy są identyczne"


def pokaz_roznice(obraz_wejsciowy):
    t_wynik = np.array(obraz_wejsciowy, dtype=np.uint8)

    max_values = []
    if obraz_wejsciowy.mode == "RGB" or obraz_wejsciowy.mode == "RGBA":
        for i in range(3):
            max_values.append(t_wynik[:, :, i].max())

        for i in range(t_wynik.shape[0]):
            for j in range(t_wynik.shape[1]):
                    for k in range(3):
                        t_wynik[i][j][k] = t_wynik[i][j][k] / max_values[k] * 255
        return Image.fromarray(t_wynik)

    elif obraz_wejsciowy.mode == "L":
        max_value = t_wynik.max()

        for i in range(t_wynik.shape[0]):
            for j in range(t_wynik.shape[1]):
                t_wynik[i][j] = t_wynik[i][j] / max_value * 255
        return Image.fromarray(t_wynik)

    return False


def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n, kolor):
    tab_obraz_wstawiany = np.asarray(obraz_wstawiany).astype(np.uint8)
    tab_obraz_bazowy = np.asarray(obraz_bazowy).astype(np.uint8)
    h0, w0 = tab_obraz_wstawiany.shape
    h1, w1 = tab_obraz_bazowy.shape[:2]

    n_k = min(h1, n + h0)  # jesli wstawiany obraz wychodzi poza ramy nowego obrazu, to przycinamy
    m_k = min(w1, m + w0)  # jesli wstawiany obraz wychodzi poza ramy nowego obrazu, to przycinamy
    n_p = max(0, n)  # jesli miejsce wstawienia jest ujemne(wychodzi poza nowy obraz w górę), to przycinamy
    m_p = max(0, m)  # jesli miejsce wstawienia jest ujemne(wychodzi poza nowy obraz w lewo), to przycinamy
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            if tab_obraz_wstawiany[i - n][j - m] == 0:
                tab_obraz_bazowy[i][j] = kolor

    return Image.fromarray(tab_obraz_bazowy)


beksinski = Image.open("beksinski.png")
beksinski1 = Image.open("beksinski1.png")
beksinski2 = Image.open("beksinski2.png")
beksinski3 = Image.open("beksinski3.png")

""" Zad 6a """
print("beksinkski = beksinski1 ->", ocen_czy_identyczne(beksinski, beksinski1))
print("beksinkski = beksinski2 ->", ocen_czy_identyczne(beksinski, beksinski2))
print("beksinkski = beksinski3 ->", ocen_czy_identyczne(beksinski, beksinski3))

""" Zad 7 """
im_jpg3 = Image.open("Sebastian_Adamus2.jpg")
im = Image.open("Sebastian_Adamus.png")
diff = ImageChops.difference(im, im_jpg3)

plt.figure(figsize=(16, 16))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.title("im")
plt.imshow(im)
plt.axis('off')
plt.subplot(2,2,2)
plt.title("im_jpg3")
plt.imshow(im_jpg3)
plt.axis('off')
plt.subplot(2,2,3)
plt.title("diff")
plt.imshow(diff)
plt.axis('off')
plt.subplot(2,2,4)
plt.title("pokaz_roznice")
plt.imshow(pokaz_roznice(diff))
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.25)
plt.savefig('fig2.png')
plt.show()

""" Zad 8 """
inicjaly = Image.open("inicjaly.bmp")
obraz_inicjaly = wstaw_inicjaly(im, inicjaly, 430, int(im.size[1]/2 - 25), [255,0,255])
obraz_inicjaly.save("obraz_inicjaly.png")