import sys

# Diccionario con los productos y sus precios
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

# Función para filtrar productos según un umbral y un modo
def filtrar_productos(umbral, modo='mayor'):
    if modo == 'mayor':
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio > umbral}
    elif modo == 'menor':
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio < umbral}
    else:
        return "Lo sentimos, no es una operación válida"
    
    return productos_filtrados

# Función principal
def main():
    # Obtener los argumentos de la línea de comandos
    args = sys.argv[1:]
    
    # Verificar que se haya ingresado al menos un argumento
    if len(args) == 0:
        print("Debe ingresar al menos un argumento.")
        return
    
    # Obtener el umbral y el modo de filtrado (mayor o menor)
    umbral = int(args[0])
    modo = args[1] if len(args) > 1 else 'mayor'
    
    # Filtrar los productos
    productos_filtrados = filtrar_productos(umbral, modo)
    
    # Imprimir los resultados
    if isinstance(productos_filtrados, str):
        print(productos_filtrados)
    else:
        print("Los productos", modo + "es al umbral son:", ', '.join(productos_filtrados.keys()))

if __name__ == "__main__":
    main()