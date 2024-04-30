# Definición de la función para calcular el factorial
def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Definición de la función para calcular la productoria
def calcular_productoria(lista):
    productoria = 1
    for elemento in lista:
        productoria *= elemento
    return productoria

# Función principal para controlar los cálculos
def calcular(**kwargs):
    for key, value in kwargs.items():
        if 'fact_' in key:
            factorial = calcular_factorial(value)
            print(f"El factorial de {value} es {factorial}")
        elif 'prod_' in key:
            productoria = calcular_productoria(value)
            print(f"La productoria de {value} es {productoria}")

# Ejemplo de uso de la función calcular
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)