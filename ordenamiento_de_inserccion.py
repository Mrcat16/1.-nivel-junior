def ordenamiento_insercion(arr):
    n = len(arr)
    for i in range(1, n):
        clave = arr[i]
        j = i -1
        while j >= 0 and arr[j] > clave:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = clave
lista=[8,15,2,1,25,7,544,65,7454,66]
ordenamiento_insercion(lista)
print(lista)