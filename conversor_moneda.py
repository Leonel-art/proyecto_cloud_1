
# 1. Definicion de la Funcion (La Licuadora)
# 'def' define la funcion. Los nombres entre parentesis son los ingredientes (parametros).
def cordobas_a_usd(costo, tasa):
    # Calcula el costo
    costo_usd = costo / tasa
    # 'return' devuelve el resultado final de la funcion
    return costo_usd

# ----------------------------------------------------

# 2. Uso de la Funcion (Haciendo el Smoothie)

# Variables
costo_hp_omen = 58776  # Precio de la HP Omen
tasa_cambio_actual = 36.6

# Llamar a la funcion y guardar el resultado
costo_convertido = cordobas_a_usd(costo_hp_omen, tasa_cambio_actual)

# 3. Mostrar el Resultado
print(f"El costo de la HP Omen (C$ {costo_hp_omen}) es:")
# Usamos el resultado que la funcion nos devolvio
print(f"Aproximadamente USD ${costo_convertido:.2f}") 

# Reutilizando la funcion: Cuanto es C$ 10,000?
costo_ejemplo = cordobas_a_usd(10000, 36.6)
print("-" * 20)
print(f"C$ 10,000.00 son aproximadamente USD ${costo_ejemplo:.2f}") 
