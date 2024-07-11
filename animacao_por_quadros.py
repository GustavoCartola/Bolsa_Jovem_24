import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Configurações iniciais
fig, ax = plt.subplots()
ax.set_xlim(0, 10)  # Defina os limites do eixo x
ax.set_ylim(0, 10)  # Defina os limites do eixo y

# Crie uma estrela inicial
pontos_estrela = np.array([[5, 6], [5.5, 4], [7, 4], [5.8, 3], [6.2, 1],
                        [5, 2], [3.8, 1], [4.2, 3], [3, 4], [4.5, 4]])
estrela = plt.Polygon(pontos_estrela, closed=True, color='black')
ax.add_patch(estrela)

def update(frame):
    # Gire a estrela
    angulo = frame * 0.1
    rotacao_matrix = np.array([[np.cos(angulo), -np.sin(angulo)],
                                [np.sin(angulo), np.cos(angulo)]])
    pontos_estrela_girado = np.dot(pontos_estrela - [5, 5], rotacao_matrix) + [5, 5]
    estrela.set_xy(pontos_estrela_girado)
    return estrela,

# Crie a animação
ani = FuncAnimation(fig, update, frames=range(100), repeat=True)

# Exiba a animação
plt.show()
