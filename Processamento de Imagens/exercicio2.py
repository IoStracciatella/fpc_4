import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import random

imagem_nome = 'stinkbug.png'
imagem = mpimg.imread(imagem_nome)

# Joga a imagem pra B&W
if len(imagem.shape) == 3:
    imagem = np.mean(imagem, axis=2)

altura, largura = imagem.shape

num_manchas = 50
raio_max = 20 

for _ in range(num_manchas):
    # Posições. Não pode ser colado na margem
    x_centro = random.randint(0, altura - 1)
    y_centro = random.randint(0, largura - 1)

    raio = random.randint(5, raio_max)

    cor = random.randint(0 , 1)

    # Aplicar a mancha
    for x in range(altura):
        for y in range(largura):
            if (x - x_centro)**2 + (y - y_centro)**2 <= raio**2:
                imagem[x, y] = cor

# Salvar e exibir a imagem modificada
plt.imshow(imagem, cmap='gray')
plt.axis('off')
plt.show()
