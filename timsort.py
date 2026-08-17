def timsort(arr):
    for i in range(1, 11):
        while True:
            try:
                corredores = int(input(f"Ingrese el tiempo del {i} corredor: "))
                print()
                arr.append(corredores)
                break
            except ValueError:
                print()
                print("Error porfa ingrese numeros interos")
                print()
    arr.sort()
lista = []
timsort(lista)
print()
for i, x in enumerate(lista[:3] ,1):
    print(f"{i} = {x}")
print()