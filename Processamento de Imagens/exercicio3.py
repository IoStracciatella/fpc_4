import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

nIteracoes = int(input('Quantas iterações de suavização você quer aplicar? n: '))

# Requer sobrecargas de, uma matriz, e quantas vezes vc quer iterar a suavização
def suavizar(imagem, iteracoes):
    
    # Converte a imagem para escala de cinza, caso ela ainda esteja colorida
    if len(imagem.shape) == 3: #"Se tiver dimensão de cor"
        imagem = np.mean(imagem, axis=2) #"Transforme em uma imagem com só 2 dimensões, sem cor"
    
    linhas, colunas = imagem.shape
    
    # Copia a imagem original p suavizar depois (não daria certo só referenciar a mesma imagem)
    imgCopia = np.copy(imagem)
    
    for _ in range(iteracoes):

        # Novo array (com a imagem) para armazenar uma iteração
        img_temp = np.copy(imgCopia)
        
        for i in range(1, linhas-1):
            for j in range(1, colunas-1):
                img_temp[i, j] = (imgCopia[i, j] + imgCopia[i+1, j] + imgCopia[i-1, j] + imgCopia[i, j+1] + imgCopia[i, j-1]) / 5
        
        # Atualizando com novos valores
        imgCopia = img_temp
    
    return imgCopia

image = mpimg.imread('stinkbug.png')

img_suavizada = suavizar(image, iteracoes=nIteracoes)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Suavizada')
plt.imshow(img_suavizada, cmap='gray')

plt.show()
