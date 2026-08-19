def timsort(arr): # Creamos la funcion timsort
    for i in range(1,11): # Creamos un bucle for para que se repita 10 veces
        while True: # Creamos el while True para poder aplicar el try y except
            try:
                corredores = int(input(f"Ingrese el tiempo del corredor numero {i}: ")) # Solicitamos al usuario que ingrese el tiempo del corredor y lo convertimos a entero
                print()
                arr.append(corredores) # Agregamos el tiempo del corredor a la lista arr
                break
            except ValueError:
                print()
                print("Error porfa solo ingrese numeros enteros") # Si el usuario ingresa un valor que no es un numero entero, se le mostrara este mensaje de error
                print()
    arr.sort() # Ordenamos la lista arr de menor a mayor
lista = [] # Creamos una lista vacia para almacenar los tiempos de los corredores
timsort(lista) # Hacemos que la funcion timsort se ejecute y le pasamos la lista vacia como parametro
print(f"Primeros 3 corredores") # Mostramos un mensaje donde indicamos que se mostraran los primeros 3 corredores
for i,x in enumerate(lista[:3], start=1): # Hacemos un bucle for para recorrer la lista y solo mostrar a los 3 primeros corredores que hicieron el menor tiempo
    print(f"El corredor {i} tiene un tiempo de {x} segundos") # Mostramos un mensaje donde indicamos el numero del corredor y su tiempo en segundos