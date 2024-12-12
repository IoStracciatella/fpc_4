import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

nIteracoes = int(input('Quantas iterações de suavização você quer aplicar? n: '))

# Sobrecargas: uma matriz, qtas vezes vc quer iterar
def suavizar(imagem, iteracoes):
    
    # B&W
    if len(imagem.shape) == 3: 
        imagem = np.mean(imagem, axis=2)
    
    linhas, colunas = imagem.shape
    
    # Não daria certo só referenciar a mesma imagem, tem q copiar
    imgCopia = np.copy(imagem)
    
    for _ in range(iteracoes):

        # Array temp da imagem p cada iteração 
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
