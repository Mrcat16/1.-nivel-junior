import random # Super importante ya que con este haremos que los numeros que nos proporciones el programa sean aleatorios
import time
import sys

# Aumentamos el límite de recursión por si prueban Merge Sort con N muy grandes
sys.setrecursionlimit(200000)

# ==========================================
# 1. ALGORITMOS DE ORDENAMIENTO
# ==========================================

# Creamos la funcion del ordenamiento burbuja
def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Creamos la funcion del ordenamiento inserccion
def ordenamiento_insercion(arr):
    n = len(arr)
    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr

# Creamos la funcion del ordenamiento seleccion
def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Creamos la funcion del marge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    izquierda = merge_sort(arr[:mid])
    derecha = merge_sort(arr[mid:])
    
    return merge(izquierda, derecha)

# Creamos la funcion del timsort
def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


# ==========================================
# 2. EVALUADOR Y BENCHMARKING
# ==========================================

def medir_tiempo(algoritmo, datos):
    # Hacemos una copia para no alterar la lista original
    datos_copia = datos.copy()
    
    inicio = time.perf_counter()
    algoritmo(datos_copia)
    fin = time.perf_counter()
    
    return fin - inicio

def ejecutar_laboratorio():
    print("=" * 60)
    print(" 🧪 LABORATORIO DE RENDIMIENTO: ALGORITMOS DE ORDENAMIENTO")
    print("=" * 60)
    
    try:
        n = int(input("\n👉 Ingrese la cantidad de números a ordenar (ej. 1000, 5000, 10000): "))
    except ValueError:
        print("❌ Por favor, ingrese un número entero válido.") # Este mensaje sale si al ingresar un numero decimal o una letra
        return

    print(f"\n🔄 Generando {n} números aleatorios...")
    datos_originales = [random.randint(1, 1000000) for _ in range(n)]

    # OJO muy impotante le damos unos nombres a los ordenamientos para asi solamente escribiendo el nombre ingresado le podamos dar una modificacion
    algoritmos = {
        "Burbuja (Bubble Sort)": ordenamiento_burbuja,
        "Inserción (Insertion Sort)": ordenamiento_insercion,
        "Selección (Selection Sort)": ordenamiento_seleccion,
        "Merge Sort (Divide y Vencerás)": merge_sort,
        "Python Built-in (Timsort)": sorted
    }

    print("\n" + "-" * 60)
    print(f"{'ALGORITMO':<32} | {'TIEMPO EN SEGUNDOS':<20}")
    print("-" * 60)

    # Advertencia si N es muy grande para cuadráticos
    limite_cuadratico = 15000 # Esto es lo que nos limita los ordenamientos burbuja,inserccion y seleccion

    for nombre, funcion in algoritmos.items():
        es_cuadratico = nombre in ["Burbuja (Bubble Sort)", "Inserción (Insertion Sort)", "Selección (Selection Sort)"] # Aqui lo agregamos para el for para cuando superen el limite impuesto se omitan (DATO: tambien funcionara el limite si agregamos los ordenamientos marge sort y timsort OJO solo los nombres que le asignamos)
        
        if n > limite_cuadratico and es_cuadratico:
            print(f"{nombre:<32} | ⚠️ Omitido (> {limite_cuadratico} elementos)") # Con esto ya directamente nos saldra que el limite a sido superado a sido omitido 
            continue

        tiempo = medir_tiempo(funcion, datos_originales)
        print(f"{nombre:<32} | ⏱️  {tiempo:.6f} s")

    print("-" * 60)

if __name__ == "__main__":
    ejecutar_laboratorio()