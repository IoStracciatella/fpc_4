import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('stinkbug.png')
A = img[:, :, 0]

print('-' * 30)
print('Qual imagem você quer exibir?')
print('-' * 30)
n = int(input('1. Imagem original\n2. Canal vermelho\n3. Canal vermelho com cmap "hot"\n4. Canal vermelho com cmap "nipy_spectral"'))

if (n == 1):
    # Mostra a imagem original
    plt.imshow(img)
    plt.title("Imagem Original")
    plt.axis('off')
    plt.show()
elif (n == 2):
    # Mostra o canal vermelho
    plt.imshow(A)
    plt.title("Canal Vermelho (Sem cmap)")
    plt.axis('off')
    plt.show()
elif (n == 3):
    # Mostra o canal vermelho com cmap "hot"
    plt.imshow(A, cmap="hot")
    plt.title("Canal Vermelho (cmap=hot)")
    plt.axis('off')
    plt.show()
elif (n == 4):
    # Mostra o canal vermelho com cmap "nipy_spectral"
    plt.imshow(A, cmap="nipy_spectral")
    plt.title("Canal Vermelho (cmap=nipy_spectral)")
    plt.axis('off')
    plt.show()
else:
    print('Insira um valor válido!') 
