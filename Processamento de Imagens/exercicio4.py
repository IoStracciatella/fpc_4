import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import random

img_original = mpimg.imread('concrete.jpg')
# B&W
if len(img_original.shape) == 3:
    img_original = np.mean(img_original, axis=2)

img_recortada = img_original[random.randint(75, 100):200, random.randint(100, 150):250]
    
limiar = 128
# Clamp na imagem pra que de pra identificar facilmente o agregado
img_util = (img_recortada > limiar) * 1.0

pixels_brancos = 0
pixels_pretos = 0

linhas, colunas = img_util.shape  # Obtém as dimensões da imagem

for i in range(linhas):
    for j in range(colunas):
        if img_util[i, j] == 1.0:
            pixels_brancos += 1
        elif img_util[i, j] == 0.0:
            pixels_pretos += 1

qtde_agregado = pixels_pretos/img_util.size
print(qtde_agregado*100)

plt.imshow(img_recortada, cmap='gray')
plt.show()
