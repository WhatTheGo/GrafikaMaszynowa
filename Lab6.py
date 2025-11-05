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
    tablica_wynikowa = np.array(obraz_wejsciowy, dtype=np.uint8)

    max_values = []
    if obraz_wejsciowy.mode == "RGB" or obraz_wejsciowy.mode == "RGBA":
        for i in range(tablica_wynikowa.shape[2]):
            max_values.append(tablica_wynikowa[:, :, 0].max())
        for i in range(tablica_wynikowa.shape[0]):
            for j in range(tablica_wynikowa.shape[1]):
                    for k in range(tablica_wynikowa.shape[2]):
                        tablica_wynikowa[i][j][k] = tablica_wynikowa[i][j][k] / max_values[k] * 255
        return Image.fromarray(tablica_wynikowa)

    return False

beksinski = Image.open("beksinski.png")
beksinski1 = Image.open("beksinski1.png")
beksinski2 = Image.open("beksinski2.png")
beksinski3 = Image.open("beksinski3.png")

""" Zad 6a """
print("beksinkski = beksinski1 ->", ocen_czy_identyczne(beksinski, beksinski1))
print("beksinkski = beksinski2 ->", ocen_czy_identyczne(beksinski, beksinski2))
print("beksinkski = beksinski3 ->", ocen_czy_identyczne(beksinski, beksinski3))

""" Zad 7 """
obrazek = Image.open("Sebastian_Adamus2.jpg")
obrazek2 = Image.open("Sebastian_Adamus.png")
diff = ImageChops.difference(obrazek, obrazek2)
pokaz_roznice(diff).show()