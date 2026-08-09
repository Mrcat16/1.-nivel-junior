numeros = [23,11,99,22] # creamos una lista de numeros enteros
for i in range(len(numeros)): # el i es el que va a ir recorriendo la lista numeros vale 0 y va ir incrementando hasta que llegue al tamaño de la lista todo esto controlado por el (len(numeros)) que len vale 4 porque la lista tiene 4 elementos
    for j in range(len(numeros)-1-i): # j va tomar son valores desde 0 hasta el tamaño de la lista menos 1 es para que la lista no compare el ultimo numero de la lista con uno que no existe, menos i, esto es para que no se compare con los elementos ya ordenados
        if numeros[j] > numeros[j+1]: # si el numero en la posicion j es mayor que el numero en la posicion j+1, entonces se hace un intercambio de valores
            # intercambio de valores
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j] # intercambiamos los valores de la posicion j y j+1, esto es para que el numero mayor se vaya al final de la lista y el menor se quede en la posicion j
print(f"Los números ordenados son: {numeros}") # aqui imprimimos la lista de numeros ya ordenada