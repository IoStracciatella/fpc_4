import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def grade_inic(N):
    grade = np.zeros((N, N))
    # Ctr (fica na metade dos dois eixos, por isso //2)
    grade[N//2, N//2] = 1 
    # Obstáculos
    num_obstaculos = N * N // 2 # N * N ficaria muita coisa
    for _ in range(num_obstaculos):
        x, y = np.random.randint(0, N, 2)
        if (x == N // 2 and y == N // 2):
            continue # Previne
        grade[x, y] = 2
    return grade

def update(grade):
    nova_grade = grade.copy()
    for i in range(1, grade.shape[0] - 1):
        for j in range(1, grade.shape[1] - 1):
            if grade[i, j] == 1:
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if grade[x, y] == 0:
                        nova_grade[x, y] = 1
    return nova_grade

grade = grade_inic(50)

fig, ax = plt.subplots()
cax = ax.matshow(grade, cmap="Blues", vmin=0, vmax=2)

def animar(frame):
    global grade
    grade = update(grade)
    cax.set_array(grade)
    return [cax]

ani = FuncAnimation(fig, animar, frames=50, interval=100, blit=True)
plt.title('Alagamento!')
plt.show()
