def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[min_idx]:
                min_idx = j
        arr[j], arr[min_idx] = arr[min_idx], arr[j]
lista = [112,45,65,88]
print()
print("Lista ordenada de menor a mayor")
print()
ordenamiento_seleccion(lista)
for i, x in enumerate(lista,1):
    print(f"{i} = {x}")

def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[j], arr[min_idx] = arr[min_idx], arr[j]
lista = [112,45,65,88]
print()
print("Lista ordenada de mayor a menor")
print()
ordenamiento_seleccion(lista)
for i, x in enumerate(lista,1):
    print(f"{i} = {x}")