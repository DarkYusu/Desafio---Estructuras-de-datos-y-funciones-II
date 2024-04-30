# Lista de velocidades de las correas transportadoras
velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
             14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22,
             14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5,
             23, 20, 23, 21]

# Función para calcular el promedio de una lista de velocidades
def calcular_promedio(velocidades):
    total = sum(velocidades)  # Suma de todas las velocidades
    promedio = total / len(velocidades)  # Promedio = suma / cantidad
    return promedio

# Función para listar las posiciones de las correas por encima del promedio
def correas_sobre_promedio(velocidades, promedio):
    posiciones = [i for i, velocidad in enumerate(velocidades) if velocidad > promedio]
    return posiciones

# Función principal
def main():
    promedio = calcular_promedio(velocidad)
    posiciones = correas_sobre_promedio(velocidad, promedio)
    print(posiciones)

if __name__ == "__main__":
    main()