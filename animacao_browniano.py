import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros
num_passos = 1000  # Número de passos
tempo = 0.01       # Intervalo de tempo

# Gerando deslocamentos aleatórios
deslocamentos = np.random.normal(0, np.sqrt(tempo), num_passos)
posicoes = np.cumsum(deslocamentos)

# Configuração da animação
fig, ax = plt.subplots()
linha, = plt.plot([], [], lw=2)
ax.set_xlim(0, num_passos)
ax.set_ylim(np.min(posicoes), np.max(posicoes))
ax.set_title("Animação do Movimento Browniano")

def init():
    linha.set_data([], [])
    return linha,

def animado(i):
    x = np.arange(i)
    y = posicoes[:i]
    linha.set_data(x, y)
    return linha,

# Criando a animação
ani = FuncAnimation(fig, animado, frames=num_passos, init_func=init, blit=True)
plt.show()