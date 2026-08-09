menu_cafeteria = {
    "Cafe": (1,0, "Bebida"),
    "Taco": (3,0, "Comida"),
    "Pepsi": (2,0, "Bebida"),
    "Pizza": (5,0, "Comida"),
}   
carrito = []
def ver_menu():
    print()
    print("Menu")
    for i, x in enumerate(menu_cafeteria,1):
        print(f"{i}.{x}")
        print()
def comprar_producto():
    print()
    print("Que desea comprar?")
    print()
    for i, x in enumerate(menu_cafeteria,1):
            print(f"{i}.{x}")
    print()
    comprar = input("").capitalize().strip()
    while comprar not in menu_cafeteria:
        print("Error porfa solo seleccione algo del menu")
        for i, x in enumerate(menu_cafeteria,1):
                    print(f"{i}.{x}")
        print()
        comprar = input("").capitalize().strip()
    if comprar in menu_cafeteria:
        carrito.append(comprar)
        print()
        print(f"Su compra {comprar} esta en el carrito")
        print()
def eliminar_producto():
    print()
    print("Que comprar desea borrar del carrito?")
    for i, x in enumerate(carrito,1):
        print(f"{i}.{x}")
    print()
    eliminar = input ("").capitalize().strip()
    if eliminar in carrito:
        carrito.remove(eliminar)
        print()
        print(f"Su compra {eliminar} se ha eliminado del carrito")
        print()
    else:
        print(f"SU compra {eliminar} no esta en el carrito")
def ver_carrito():
    print()
    total=0
    for i, x in enumerate(carrito,1):
        precio = menu_cafeteria[x][0]
        print(f"{i}.{x} - ${precio:.0f}")
        total += precio
    print()
    print(f"Total del carrito - ${total:.0f}")
    print()
def salirr():
    print()
    print("SEguro que quiere salir del programa?")
    print("si o no")
    salir = input("").lower().strip()
    while salir not in ["si", "no"]:
        print("Error porfa solo escriba si o no")
        salir = input("").lower().strip()
    if salir == "si":
        print()
        print("Gracias por usar el programa")
        return True
    else:
        print()
        print("Volviendo al programa")
        print()
        return False
while True:
    print("Elije una de las siguientes opciones")
    print()
    print("1.Ver Menu")
    print("2.Comprar")
    print("3.Eliminar Compra")
    print("4.Ver Carrito")
    print("5.Salir")
    print()
    opcion = input("")
    if opcion == "1":
        ver_menu()
    elif opcion == "2":
        comprar_producto()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        ver_carrito()
    elif opcion == "5":
        if salirr():
            break
    else:
        print()
        print("Error opcion no valida solo seleccione las opciones disponibles")
        print()