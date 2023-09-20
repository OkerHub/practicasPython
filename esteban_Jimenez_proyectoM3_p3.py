import random
import matplotlib.pyplot as plt

def simular_canicas(num_canicas, num_niveles):
    contenedores = [0] * (num_niveles + 1)

    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            direccion = random.choice([-1, 1])  # -1 representa izquierda, 1 representa derecha
            posicion += direccion
        contenedores[posicion] += 1

    return contenedores

def graficar_histograma(contenedores):
    plt.bar(range(len(contenedores)), contenedores, color='blue')
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de Canicas')
    plt.title('Simulación de Máquina de Galton')
    plt.show()

# Simulación de 3000 canicas y 12 niveles
resultados = simular_canicas(3000, 12)

# Graficar el histograma
graficar_histograma(resultados)
