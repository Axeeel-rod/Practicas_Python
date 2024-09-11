import matplotlib.pyplot as plt
import numpy as np
import random

canicas = 3000
niveles = 12

def simular_canicas(canicas, niveles):
    contenedores = np.zeros(niveles + 1)  
    for _ in range(canicas):
        posicion = 0  
        for _ in range(niveles):
            if random.random() >= 0.5:
                posicion += 1
                
        contenedores[posicion] += 1
    return contenedores

def graficar_histograma(contenedores):
    plt.bar(range(len(contenedores)), contenedores, color='green', edgecolor='grey')
    plt.title('Maquina de Galton')
    plt.xlabel('Contenedores')
    plt.ylabel('Número de canicas')
    plt.show()

resultados = simular_canicas(canicas, niveles)
graficar_histograma(resultados)
