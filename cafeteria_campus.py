# programa que sirve para pedir comida y bebida en una cafeteria en un totem (osea de forma de menu virtual donde el usuario puede pedirlo obviamente pagando tambien)
# Creamos una tupla con nuestros productos
menu_cafeteria = {
    "Cafe Latte": (1.0, "Bebida"),
    "Pan": (1.0, "Comida"),
    "Taco": (2.0, "Comida"),
    "Pepsi": (3.0, "Bebida")
}
carrito = [] # Creamos la lista de nuestro carrito

def ver_menu():
    # Esto lo hacemos de esta forma para que el usuario pueda ver nuestros productos de forma ordenada
    print()
    for i, x in enumerate (menu_cafeteria,1):
        print(f"{i}.{x}")
    print()
def pedir_producto():
    # Aqui el usuario puede añadir uno de nuestros productos a su carrito y le vo,vemos a mostrar el menu para que mire lo que tenemos disponible
    print()
    print("Menu")
    for i, x in enumerate (menu_cafeteria,1):
        print(f"{i}.{x}")
    print()
    pedir = input("Que producto de la cafeteria desea añadir al carrito?: ").title().strip() 
    while pedir not in ["Cafe Latte","Pan", "Taco", "Pepsi"]:
        # si el usuario se equivoca le pedimos que seleccione solo los productos que se le muestran en pantalla
        print("Error porfa solo seleccione uno de los productos disponibles")
        for i, x in enumerate (menu_cafeteria,1):
            print(f"{i}.{x}")
        pedir = input("").title().strip()
        print()
    if pedir in menu_cafeteria: # Esto funciona de manera que si el producto esta en el menu_cafeteria se agregue al carrito
        carrito.append(pedir)
        print()
        print(f"Se guardo {pedir} correctamente en el carrito")
        print()
def ver_carito_total():
    # Este sirve para ver tu carrito y el total a pagar
    print()
    total = 0
    print("Productos en tu Carrito")
    for s, d in enumerate (carrito,1):
        precio = menu_cafeteria[d][0] # aqui una cosa la variable ese 0 funcina ya que busca el numero 0 en la tupla
        print(f"{s}. {d} - ${precio:.1f}") # Aqui controlamos para que se vea en orden del 1 en adelante y que se muestre solamente una decimal
        total += precio # el total de todo
    print()
    print(f"Total a pagar: ${total:.1f}") 
    print()
    return total
def borrar_carrito():
    # Esto sirve por si no quieres un producto no o no quieres comprar nada lo puedas borrar del carrito
    print()
    producto_borrar = input ("QUe producto Deseas eliminar del carrito?: ").title().strip()
    print()
    if producto_borrar in carrito:
        # Si el producto si esta en el menu lo borrar del carito
        print()
        carrito.remove(producto_borrar)
        print(f"El producto {producto_borrar} se a borrado correctamente del carrito:")
        print()
    else:
        print()
        print(f"El produto {producto_borrar} no se encuentra en el carrito:") # Pero si no esta sale el mensaje de que bueno no esta :/
        print()
def salir():
    # Aqui simplemente te preguntamos si estas seguro de salir del totem de la cafeteria
    print()
    print("Seguro que quiere salir del programa de la cafeteria?: ")
    print("si o no")
    sali = input("").lower().strip()
    while sali not in ["si", "no"]:
        print()
        print("Error porfa solo escriba si o no") # Si el usuario se equivoca le pedimos que solo escriba si o no
        sali = input("").lower().strip()
    if sali == "si":
        print()
        print("Gracias por usar el programa de la cafeteria:") # SI es si le damos las gracias por usar el totem y se cerrara el totem de la cafeteria
        print()
        return True # Esto sirve por si el usuario confirma que quiere salir del totem rompa el ciclo y lo deje salir
    else:
        print()
        print("Volviendo al programa:") 
        print()
    return False # Esto sirve por si el usuario decide no salir del programa y continuar haciendo que lo devuelva al totem
while True:
    # Aqui le damos las opciones para que el usuario decide que quiere eligir
    print("1.Ver Menu")
    print("2.Pedir Producto")
    print("3.Ver Carrito y Total")
    print("4.Borrar producto del carrito")
    print("5.Salir")
    print()
    opcion = input("Elija una de las opciones disponibles: ").strip()
    print()
    if opcion == "1":
        ver_menu()
    elif opcion == "2":
        pedir_producto()
    elif opcion == "3":
        ver_carito_total()
    elif opcion == "4":
        borrar_carrito()
    elif opcion == "5":
# Al final le mostramos su carrito mas la opcion de volver al programa y de pagar el carrito
        print()
        total_final = ver_carito_total()
        if total_final > 0:
            print("si o no")
            print("Desea proceder al pago?:")
            pago = input("").lower().strip()
            while pago not in ["si", "no"]:
                print()
                print("Error porfa solo escriba si o no")
                pago = input("").lower().strip()
            if pago == "si":
                print()
                print(f"Pago de $ {total_final:.1f} a sido exitoso gracias por usar el programa de la cafeteria de la universidad")
                carrito.clear()
                print()
                break
        if salir():
            break
    else:
        print()
        print("Opcion no valida")
        print()