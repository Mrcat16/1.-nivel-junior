def algoritmo_inserccion(arr):
    corredor = int(input("Ingrese el tiempo del 1 Corredor: "))
    arr.append(corredor)
    corredor2 = int(input("Ingrese el tiempo del 2 Corredor: "))
    arr.append(corredor2)
    corredor3 = int(input("Ingrese el tiempo del 3 Corredor: "))
    arr.append(corredor3)
    corredor4 = int(input("Ingrese el tiempo del 4 Corredor: "))
    arr.append(corredor4)
    corredor5 = int(input("Ingrese el tiempo del 5 Corredor: "))
    arr.append(corredor5)
    corredor6 = int(input("Ingrese el tiempo del 6 Corredor: "))
    arr.append(corredor6)
    corredor7 = int(input("Ingrese el tiempo del 7 Corredor: "))
    arr.append(corredor7)
    corredor8 = int(input("Ingrese el tiempo del 8 Corredor: "))
    arr.append(corredor8)
    corredor9 = int(input("Ingrese el tiempo del 9 Corredor: "))
    arr.append(corredor9)
    corredor10 = int(input("Ingrese el tiempo del 10 Corredor: "))
    arr.append(corredor10)
    n = len(arr)
    for i in range(1, n):
        clave = arr[i]
        j = i-1
        while j >=0 and arr[j] > clave:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = clave
lista = []
algoritmo_inserccion(lista)
for i, x in enumerate(lista[:3],1):
    print(f"{i} = {x}")