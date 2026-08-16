def corredores_inserccion(arr):
    # 1. Pedimos los datos y los guardamos directamente en 'arr'
    corredor = float(input("Ingrese el tiempo del primer corredor: "))
    arr.append(corredor)
    corredor2 = float(input("Ingrese el tiempo del segundo corredor: "))
    arr.append(corredor2)
    corredor3 = float(input("Ingrese el tiempo del tercer corredor: "))
    arr.append(corredor3)
    
    # 2. Algoritmo de Inserción
    n = len(arr)
    for i in range(1, n):
        clave = arr[i]  # Corregido: Se usan corchetes [] para indices
        j = i - 1
        while j >= 0 and arr[j] > clave:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = clave  # Corregido: Va afuera del ciclo 'while'

# --- Bloque Principal ---
lista = []

# ¡Importante! Aquí llamamos a la función para que pida los datos y ordene
corredores_inserccion(lista)

print()
print("Primeros 3 Puestos")
print()
for i, x in enumerate(lista, 1):
    print(f"{i}. {x:.0f}")
print()