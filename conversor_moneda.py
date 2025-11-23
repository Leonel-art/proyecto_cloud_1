
# 1. Definicion de la Funcion (La Receta)
def cordobas_a_usd(costo, tasa):
    # Calcula el costo
    costo_usd = costo / tasa
    # Devuelve el resultado
    return costo_usd

# 2. Variables de Control
TASA_CAMBIO = 36.6

# 3. Abrir el archivo de datos y procesar linea por linea
print("--- CONVERSOR DE MONEDA AUTOMATIZADO ---")

# 'with open' asegura que el archivo se cierre automaticamente
with open('precios.txt', 'r') as archivo:
    
    # 'for linea in archivo' lee cada linea del archivo precios.txt
    for linea in archivo:
        
        # Eliminar espacios y saltos de linea
        linea = linea.strip()
        
        # Separar el nombre del producto y su costo usando ":"
        nombre, costo_str = linea.split(':')
        
        # Convertir el costo a numero entero para poder calcular
        costo_cordobas = int(costo_str)
        
        # Usar la funcion (la receta) para convertir a USD
        costo_convertido = cordobas_a_usd(costo_cordobas, TASA_CAMBIO)
        
        # Mostrar el resultado
        print(f"Producto: {nombre.strip()}")
        print(f"  C$ {costo_cordobas:,.2f} -> USD ${costo_convertido:.2f}")

print("------------------------------------------")

