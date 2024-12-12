import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def init_grid(N):
    grid = np.zeros((N, N))
    grid[N//2, N//2] = 1  # Fonte central
    # Adiciona obstáculos de forma aleatória
    num_obstacles = N * N // 10  # Aproximadamente 10% da grade
    for _ in range(num_obstacles):
        x, y = np.random.randint(0, N, 2)
        grid[x, y] = 2
    return grid

def update(grid):
    new_grid = grid.copy()
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            if grid[i, j] == 1:  # Alagar vizinhos
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if grid[x, y] == 0:
                        new_grid[x, y] = 1
    return new_grid

N = 50  # Tamanho maior da grade para melhor visualização
grid = init_grid(N)

fig, ax = plt.subplots()
cax = ax.matshow(grid, cmap="Blues", vmin=0, vmax=2)  # Melhor contraste de cores

def animate(frame):
    global grid
    grid = update(grid)
    cax.set_array(grid)
    return [cax]

ani = FuncAnimation(fig, animate, frames=50, interval=100, blit=True)
plt.title('Flooding Algorithm')
plt.show()

